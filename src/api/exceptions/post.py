from fastapi import HTTPException

def post_notfound():
    raise HTTPException(status_code=404, detail="Postagem não encontrada")