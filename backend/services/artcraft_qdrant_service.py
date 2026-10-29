"""
Serviço de Integração Aletheia <-> ArtCraft via Qdrant
Responsável por enriquecimento semântico de prompts para geração visual.
"""
import os
import json
import requests
from typing import List, Dict, Optional

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "teologia_v3_master")


class ArtCraftQdrantService:
    """Serviço responsável por buscar contexto teológico no Qdrant
    e enriquecer prompts para geração de imagens no ArtCraft."""

    def __init__(self, qdrant_url: str = None, collection: str = None):
        self.qdrant_url = qdrant_url or QDRANT_URL
        self.collection = collection or COLLECTION_NAME
        self.search_url = f"{self.qdrant_url}/collections/{self.collection}/points/search"

    def buscar_contexto_teorico(self, query: str, limit: int = 5) -> List[Dict]:
        """Busca chunks no Qdrant relacionados à query para enriquecer o contexto.
        Ex: Se o usuário pedir Moisés no Sinai, busca descrições de vestimenta,
        geografia e contexto cultural da época.
        """
        # Nota: Em produção, usaríamos um embedding real da query
        payload = {
            "vector": [0.0] * 384,
            "limit": limit,
            "with_payload": True,
            "filter": {
                "must": [
                    {"key": "tema", "match": {"value": "biblia"}}
                ]
            }
        }

        try:
            response = requests.post(self.search_url, json=payload)
            if response.status_code == 200:
                return response.json().get("result", [])
            else:
                print(f"Erro ao consultar Qdrant: {response.status_code}")
                return []
        except Exception as e:
            print(f"Falha na conexão com Qdrant: {e}")
            return []

    def enriquecer_prompt(self, user_prompt: str) -> str:
        """Consulta o Qdrant e anexa o contexto teológico ao prompt."""
        contextos = self.buscar_contexto_teorico(user_prompt)
        if not contextos:
            return user_prompt
        
        contexto_texto = " ".join([str(p.get("payload", {})) for p in contextos])
        return f"{user_prompt}\n\nContexto Teológico: {contexto_texto}"
