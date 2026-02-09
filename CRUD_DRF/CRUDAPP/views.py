from rest_framework.response import Response 
from rest_framework.decorators import api_view
from CRUDAPP.models import Students
from CRUDAPP.serializer import StudentSerializer
from rest_framework import status

#Create a POST
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
#Get all the Studnets
@api_view(['GET'])
def get_student(request):
    students = Students.objects.all()
    serializer = StudentSerializer(students, many = True)
    return Response(serializer.data)

#Read the data
@api_view(['GET'])
def student_details(request, pk):
    try:
        student = Students.objects.get(pk = pk)
    except Students.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    serializer = StudentSerializer(student)
    return Response(serializer.data, status = status.HTTP_302_FOUND)


#UPDATE - PUT/PATCH
#PUT = Update files
#PATCH = update selected field only
@api_view(['PUT'])
def update_student(request, pk):
    try:
        Student = Students.objects.get(pk = pk)
    except Students.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(Student, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# DELETE
@api_view(['DELETE'])
def delete_student(request, pk):
    student = Students.object.get(pk = pk)
    student.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)