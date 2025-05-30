from fastapi import APIRouter
from app.api.v1.endpoints import usuarios, auth, menus, roles, permisos, areas, costura, administracion

api_router = APIRouter()

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Autenticación"]
)

api_router.include_router(
    usuarios.router,
    prefix="/usuarios",
    tags=["Usuarios"]
)

api_router.include_router(
    menus.router,
    prefix="/menus",
    tags=["Menus"]
)

api_router.include_router(
    roles.router, 
    prefix="/roles", 
    tags=["Roles"]
    )

api_router.include_router(
    permisos.router, 
    prefix="/permisos", 
    tags=["Permisos (Rol-Menú)"]
    )

api_router.include_router(
    areas.router, 
    prefix="/areas", 
    tags=["Areas"]
    )

api_router.include_router(
    costura.router,
    prefix="/costura",
    tags=["Costura"]
)

api_router.include_router(
    administracion.router,
    prefix="/administracion",
    tags=["administracion"]
)