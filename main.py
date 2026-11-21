# =========================================================
# 
# Project Name : Intelligent Document Question Answering System
# using RAG and Large Language Models
#
# Author : Prajakta Shinde
# Date : 21/11/2026
#
# Description :
# This project allows the user to upload a PDF document and ask
# questions based on its content. The system uses RAG architecture,
# FAISS vector database, Sentence Transformers embeddings, and a
# local LLM through Ollama to generate context-aware answers.
#
# =========================================================
import streamlit as st
import PyPDF2
import faiss
import numpy as np
import requests

print("Jay Ganesh")