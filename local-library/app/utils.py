from pathlib import Path

from langchain_core.documents import Document


def get_info() -> list[Document]:
	data_path = Path(__file__).with_name("data.txt")
	text = data_path.read_text(encoding="utf-8")
	paragraphs = [paragraph.strip() for paragraph in text.split("\n\n") if paragraph.strip()]

	return [
		Document(
			page_content=paragraph,
			metadata={"source": str(data_path), "paragraph": index},
		)
		for index, paragraph in enumerate(paragraphs)
	]
    