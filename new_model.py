# Using Pegasus-cnn_dailymail for abstractive summarization
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch

# src_text = [
#     """ PG&E stated it scheduled the blackouts in response to forecasts for high winds amid dry conditions. The aim is to reduce the risk of wildfires. Nearly 800 thousand customers were scheduled to be affected by the shutoffs which were expected to last through at least midday tomorrow."""
# ]

def pega_sum(src_text):
    src_text = [src_text]
    model_name = 'google/pegasus-cnn_dailymail'
    torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
    batch = tokenizer.prepare_seq2seq_batch(src_text, truncation=True, padding='longest').to(torch_device)
    translated = model.generate(**batch)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    # assert tgt_text[0] == "California's largest electricity provider has turned off power to hundreds of thousands of customers."

    return tgt_text[0].replace('<n>', ' ')


# sum_text = pega_sum(src_text)
# print(sum_text)