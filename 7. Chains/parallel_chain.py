from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
# Runnable parallel - Used to execute multiple chains in parallel

load_dotenv()

model1 = ChatGroq(model="llama-3.1-8b-instant")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task="text-generation"
)
model2 = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text. \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short question and answers from the following text. \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

# Parallel Chain
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

# Sequential Chain
merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
The transformer architecture, introduced in the 2017 paper "Attention Is All You Need" by Vaswani et al., 
fundamentally changed the field of natural language processing. Unlike previous sequence-to-sequence models 
that relied on recurrent neural networks (RNNs) or long short-term memory networks (LSTMs), transformers 
process entire sequences in parallel using a mechanism called self-attention. This parallelism made 
transformers significantly faster to train on modern hardware like GPUs and TPUs.

The core idea behind self-attention is that every token in a sequence can directly attend to every other 
token, regardless of distance. For each token, the model computes three vectors: a Query (Q), a Key (K), 
and a Value (V). The attention score between two tokens is computed as the dot product of the Query of one 
token with the Key of another, scaled by the square root of the dimension size to prevent vanishing 
gradients. These scores are passed through a softmax function to produce weights, which are then used to 
compute a weighted sum of the Value vectors. This tells the model how much focus to place on each token 
when encoding a particular position.

Transformers use multi-head attention, meaning the Q, K, V computation is performed multiple times in 
parallel with different learned weight matrices. Each "head" can learn to attend to different kinds of 
relationships — one head might capture syntactic dependencies, another might capture semantic similarity, 
and another might track long-range coreference. The outputs of all heads are concatenated and projected 
through a linear layer.

Since transformers have no built-in notion of order (unlike RNNs which process tokens sequentially), 
positional encodings are added to the input embeddings to inject information about token positions. 
The original paper used fixed sinusoidal encodings, but later models like BERT and GPT use learned 
positional embeddings.

A standard transformer consists of an encoder and a decoder. The encoder processes the input sequence 
and produces a rich contextual representation for each token. The decoder generates the output sequence 
one token at a time, attending to both its own previously generated tokens (via masked self-attention) 
and the encoder's output (via cross-attention). BERT uses only the encoder (making it good for 
classification and understanding tasks), while GPT uses only the decoder (making it good for 
text generation). Models like T5 and BART use the full encoder-decoder architecture for tasks 
like translation and summarization.

Training transformers requires massive amounts of data and compute. The process typically involves 
a pretraining phase on a large unlabeled corpus (using objectives like masked language modeling in 
BERT or next-token prediction in GPT), followed by fine-tuning on a smaller labeled dataset for a 
specific downstream task. The introduction of the "pretrain then fine-tune" paradigm was a major 
shift in NLP, replacing task-specific architectures with a single general-purpose model that could 
be adapted to many tasks with minimal modification.

Scaling laws, studied extensively by researchers at OpenAI and DeepMind, show that transformer 
performance improves predictably as model size, dataset size, and compute budget increase. This 
insight drove the development of increasingly large models — from BERT's 110 million parameters 
to GPT-3's 175 billion, and beyond to models like GPT-4 and Gemini whose parameter counts are 
not publicly disclosed. These large language models exhibit emergent capabilities — behaviors that 
appear suddenly at scale and were not present in smaller versions — such as in-context learning, 
chain-of-thought reasoning, and instruction following.
"""

result = chain.invoke({'text': text})
print(result)

chain.get_graph().print_ascii()