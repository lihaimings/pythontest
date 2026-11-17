from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
md5_path = str(BASE_DIR / "md5.txt")

# Chroma
collection_name = "rag"
persist_directory = str(BASE_DIR / "chroma_db")

# spliter
chunk_size = 1000
chunk_overlap = 100
separators = ["\n\n","\n","。",",","，","!","?","？"," ","  "]
max_split_char_number = 10

similarity_threshold = 1

session_config ={
        "configurable":{
            "session_id":"user_001",
        }
    }