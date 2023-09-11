from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer

def translate_text(text):

    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fi")
    input_ids = tokenizer.encode(text, return_tensors="pt")

    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-fi")

    translated_ids = model.generate(input_ids, max_length=50, num_beams=4, early_stopping=True)
    translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)

    return translated_text

