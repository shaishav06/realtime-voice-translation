from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def translate(text, target_lang):
    if target_lang == "pt":
        model_name = f'Helsinki-NLP/opus-mt-tc-big-en-pt'
    else:
        model_name = f'Helsinki-NLP/opus-mt-en-{target_lang}'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids=input_ids, num_beams=5, num_return_sequences=3)
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)
