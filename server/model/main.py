import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

import numpy as np
import json

from huggingface_hub import login
login('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')

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def encode(text):
    return model.encode(text, normalize_embeddings=True)

def fetch_question(answer: str):
    emb = encode(answer)

    with open(os.path.join(os.curdir, 'resources\\emb.npy'), 'rb') as f:
        q_embs = np.load(f)

    cosine_scores = util.cos_sim(q_embs, emb).squeeze().numpy()

    # Make sure it's 1D
    if cosine_scores.ndim != 1:
        cosine_scores = cosine_scores.flatten()

    probabilities = np.clip(cosine_scores, 0, None)  # remove negatives
    probabilities /= probabilities.sum()


    with open(os.path.join(os.curdir, 'resources\\ques_list.json'), 'r') as f:
        questions = json.load(f)

    selected_question = np.random.choice(questions, p=probabilities)
    return selected_question


def encode_questions():
    with open(os.path.join(os.curdir, 'resources\\ques_list.json'), 'r') as f:
        data = json.load(f)

    result = []
    for q in data:
        result.append(encode(q))

    with open(os.path.join(os.curdir, 'resources\\emb.npy'), 'wb') as f:
        np.save(f, np.array(result))