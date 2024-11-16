from fastapi import APIRouter, Depends, status, HTTPException
from api.dtos.responses.standard_response_dto import StandardResponseDto
from api.repositories.user_repository import UserRepository

users_router = APIRouter()
user_repository = UserRepository()

@users_router.delete('/delete/{email}', response_model=StandardResponseDto)
async def delete_user(email: str) -> StandardResponseDto:
    print(f"Attempting to delete user with email: {email}")
    deleted = await user_repository.delete_user_by_email(email)
    print(f"User deleted: {deleted}")
    
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return StandardResponseDto(status_code=status.HTTP_200_OK,
                               status='success',
                               message=f'User with email {email} deleted successfully')

