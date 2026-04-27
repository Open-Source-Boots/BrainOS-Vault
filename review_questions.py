import os
import re
import yaml
from datetime import datetime

VAULT_ROOT = os.path.dirname(os.path.abspath(__file__))
BRAIN_ENTRIES_FOLDER = "02-BRAIN-ENTRIES"
ANSWERS_FOLDER = "06-ANSWERS"

DOMAIN_MAP = {
    "GLWC-PROJECT.md": "GLWC-PROJECT",
    "SKILLS-EDUCATION.md": "SKILLS-EDUCATION",
    "ACTIVE-PROJECTS.md": "ACTIVE-PROJECTS",
    "BRAINOS-SYSTEM.md": "BRAINOS-SYSTEM",
    "DEVICE-ECOSYSTEM.md": "DEVICE-ECOSYSTEM",
    "BRAYDEN-IDENTITY.md": "BRAYDEN-IDENTITY",
    "FINANCIAL-SNAPSHOT.md": "FINANCIAL-SNAPSHOT",
}

SKIP_TARGETS = {"FINANCIAL-SNAPSHOT.md"}

def ensure_dirs():
    for domain in DOMAIN_MAP.values():
        path = os.path.join(VAULT_ROOT, ANSWERS_FOLDER, domain)
        os.makedirs(path, exist_ok=True)

def load_questions():
    questions = []
    folder = os.path.join(VAULT_ROOT, BRAIN_ENTRIES_FOLDER)
    for fname in sorted(os.listdir(folder)):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(folder, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.startswith("---"):
            continue
        rest = content[3:]
        close = rest.find("\n---")
        if close == -1:
            continue
        fm_text = rest[:close]
        try:
            fm = yaml.safe_load(fm_text)
        except:
            continue
        if not fm or "open_questions" not in fm:
            continue
        oqs = fm["open_questions"]
        if not isinstance(oqs, list):
            continue
        for oq in oqs:
            if not isinstance(oq, dict):
                continue
            if oq.get("status", "").upper() != "OPEN":
                continue
            canonical = oq.get("canonical_target", "BRAINOS-SYSTEM.md")
            if canonical in SKIP_TARGETS:
                continue
            question_text = oq.get("question", "").strip()
            if not question_text or question_text.lower().startswith("none"):
                continue
            questions.append({
                "file": fname,
                "filepath": fpath,
                "id": oq.get("id", ""),
                "question": question_text,
                "canonical_target": canonical,
                "status": oq.get("status", "OPEN"),
            })
    return questions

def update_question_status(filepath, question_id, new_status):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split("\n")
    in_fm = False
    in_oq_block = False
    in_target_item = False
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if i == 0 and line.strip() == "---":
            in_fm = True
            new_lines.append(line)
            i += 1
            continue
        if in_fm and line.strip() == "---":
            in_fm = False
            new_lines.append(line)
            i += 1
            continue
        if in_fm and line.strip().startswith("open_questions:"):
            in_oq_block = True
            new_lines.append(line)
            i += 1
            continue
        if in_oq_block and in_fm:
            if f'id: {question_id}' in line:
                in_target_item = True
            if in_target_item and 'status:' in line:
                line = re.sub(r'status:\s*\S+', f'status: {new_status}', line)
                in_target_item = False
            if line and not line.startswith(" ") and not line.strip().startswith("-"):
                in_oq_block = False
        new_lines.append(line)
        i += 1
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(new_lines))

def get_answers_path(canonical_target, suffix="answers"):
    domain = DOMAIN_MAP.get(canonical_target, "BRAINOS-SYSTEM")
    answers_dir = os.path.join(VAULT_ROOT, ANSWERS_FOLDER, domain)
    os.makedirs(answers_dir, exist_ok=True)
    target_stem = canonical_target.replace(".md", "")
    return os.path.join(answers_dir, f"{target_stem}-{suffix}.md")

def log_entry(filepath, question_id, question_text, answer_text, source_file, label="CLOSED"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = (
        f"\n## {question_id} — {timestamp}\n"
        f"**Source:** {source_file}\n"
        f"**Question:** {question_text}\n"
        f"**Answer:** {answer_text}\n"
        f"**Status:** {label}\n"
    )
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(entry)

def print_progress(current, total, answered, skipped, saved_later):
    bar_len = 30
    filled = int(bar_len * current / total) if total > 0 else 0
    bar = "\u2588" * filled + "\u2591" * (bar_len - filled)
    print(f"\n  Progress: [{bar}] {current}/{total}")
    print(f"  \u2705 Answered: {answered}  \u23ed  Skipped: {skipped}  \U0001f550 Later: {saved_later}")

def main():
    ensure_dirs()
    questions = load_questions()
    total = len(questions)

    if total == 0:
        print("\n\u2705 No open questions found. Vault is clean.")
        return

    print(f"\n{'='*55}")
    print(f"  \U0001f9e0 BRAINOS QUESTION REVIEW")
    print(f"  {total} open questions loaded")
    print(f"  (Financial questions excluded — handled separately)")
    print(f"{'='*55}")
    print("  Controls:")
    print("  [A] Answer and close")
    print("  [S] Skip for now")
    print("  [L] Save for later")
    print("  [N] Add a note without closing")
    print("  [D] Mark duplicate / already resolved")
    print("  [Q] Quit and save progress")
    print(f"{'='*55}\n")

    answered = skipped = saved_later = 0

    for idx, q in enumerate(questions, 1):
        print_progress(idx - 1, total, answered, skipped, saved_later)
        print(f"\n  \u250c\u2500 Question {idx} of {total}")
        print(f"  \u2502  ID:      {q['id']}")
        print(f"  \u2502  Source:  {q['file']}")
        print(f"  \u2502  Target:  {q['canonical_target']}")
        print(f"  \u2514\u2500 \u2753 {q['question']}\n")

        while True:
            choice = input("  > [A]nswer  [S]kip  [L]ater  [N]ote  [D]uplicate  [Q]uit: ").strip().upper()

            if choice == "Q":
                print(f"\n{'='*55}")
                print(f"  Session ended early.")
                print_progress(idx, total, answered, skipped, saved_later)
                print(f"{'='*55}\n")
                return

            elif choice == "A":
                answer = input("  \u270f\ufe0f  Your answer: ").strip()
                if answer:
                    update_question_status(q['filepath'], q['id'], "CLOSED")
                    log_entry(
                        get_answers_path(q['canonical_target']),
                        q['id'], q['question'], answer, q['file']
                    )
                    answered += 1
                    print("  \u2705 Closed and logged.\n")
                    break
                else:
                    print("  \u26a0\ufe0f  Answer can't be blank. Try again or pick another option.")

            elif choice == "S":
                skipped += 1
                print("  \u23ed  Skipped.\n")
                break

            elif choice == "L":
                log_entry(
                    get_answers_path(q['canonical_target'], suffix="save-for-later"),
                    q['id'], q['question'], "[SAVE FOR LATER]", q['file'], label="LATER"
                )
                skipped += 1
                saved_later += 1
                print("  \U0001f550 Logged to save-for-later. Question stays open.\n")
                break

            elif choice == "N":
                note = input("  \U0001f4dd Your note: ").strip()
                if note:
                    log_entry(
                        get_answers_path(q['canonical_target']),
                        q['id'], q['question'], f"[NOTE — not closed] {note}",
                        q['file'], label="NOTE"
                    )
                    print("  \U0001f4dd Note logged. Question stays OPEN.\n")
                break

            elif choice == "D":
                update_question_status(q['filepath'], q['id'], "CLOSED")
                log_entry(
                    get_answers_path(q['canonical_target']),
                    q['id'], q['question'],
                    "[DUPLICATE / ALREADY RESOLVED — auto-closed]",
                    q['file'], label="DUPLICATE"
                )
                answered += 1
                print("  \U0001f5d1  Marked duplicate and closed.\n")
                break

            else:
                print("  \u26a0\ufe0f  Invalid. Use A, S, L, N, D, or Q.")

    print(f"\n{'='*55}")
    print(f"  \U0001f389 All questions reviewed!")
    print_progress(total, total, answered, skipped, saved_later)
    print(f"  Answers staged in: {ANSWERS_FOLDER}/")
    print(f"  Next step: review answer files and push to canonical files.")
    print(f"{'='*55}\n")

if __name__ == "__main__":
    main()
