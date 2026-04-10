from pypdf import PdfReader


def normalize_spaces(text: str) -> str:
    return " ".join(text.split())


def main() -> None:
    pdf = PdfReader("Augustin W9.pdf")

    keyword_input = input("Enter keyword: ")
    keyword = normalize_spaces(keyword_input).lower()

    match_count = 0

    for page_number, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()

        if not text:
            continue

        normalized_text = normalize_spaces(text).lower()

        if keyword and keyword in normalized_text:
            print(f"\n--- Match found on page {page_number} ---")
            print(text)
            match_count += 1

    if match_count == 0:
        print("No matches found.")
    else:
        print(f"\nTotal matching pages: {match_count}")


if __name__ == "__main__":
    main()