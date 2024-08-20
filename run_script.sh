#!/bin/bash

# OPT
python3 opt.py facebook/opt-125m c4 > output/opt/dense_baseline_output.txt
python3 opt.py facebook/opt-125m c4 --sparsity .5 > output/opt/unstructured50_sparsity_output.txt
python3 opt.py facebook/opt-125m c4 --prunen 4 --prunem 8 > output/opt/4_8_sparsity_output.txt
python3 opt.py facebook/opt-125m c4 --prunen 2 --prunem 4 > output/opt/2_4_sparsity_output.txt
python3 opt.py facebook/opt-125m c4 --sparsity .5 --wbits 16 > output/opt/unstructured50_125m_16bit_quantization_output.txt
python3 opt.py facebook/opt-125m c4 --sparsity .5 --wbits 8 > output/opt/unstructured50_125m_8bit_quantization_output.txt
python3 opt.py facebook/opt-125m c4 --sparsity .5 --wbits 4 > output/opt/unstructured50_125m_4bit_quantization_output.txt

#LLaMA
python3 llama.py meta-llama/Llama-2-13b-hf wikitext2 --sparsity .5 > output/llama/13B_50_unstructured_output.txt
python3 llama.py meta-llama/Llama-2-13b-hf wikitext2 --prunen 4 --prunem 8 > output/llama/13B_4_8_sparsity_output.txt
python3 llama.py meta-llama/Llama-2-13b-hf wikitext2 --prunen 2 --prunem 4 > output/llama/13B_2_4_sparsity_output.txt