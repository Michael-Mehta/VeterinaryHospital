from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from .models import *
from django.shortcuts import get_object_or_404
import json




# Create your views here.
def update_vet(request, vet_id):
    if request.method != 'PUT':
        return HttpResponseNotAllowed(['PUT'])

    # Manually read the body and parse it as multipart
    # Required because Django only parses multipart for POST
    if 'multipart/form-data' in request.content_type:
        # Need to manually parse the body
        from django.http.multipartparser import MultiPartParser, MultiPartParserError

        try:
            parser = MultiPartParser(request.META, request, request.upload_handlers)
            data, files = parser.parse()
        except MultiPartParserError as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Unsupported content type'}, status=400)

    vet = get_object_or_404(Pets, pk=vet_id)

    vet.name = data.get('name', vet.name)
    vet.specialization = data.get('specialization', vet.specialization)

    if 'image' in files:
        vet.image = files['image']

    vet.save()

    return JsonResponse({
        "id": vet.id,
        "name": vet.name,
        "specialization": vet.specialization,
        "image": vet.image.url if vet.image else None,
    })



def create_vet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        image = request.FILES.get('image')  

        vet = Vets.objects.create(
            name=name,
            specialization=specialization,
            image=image
        )

        return JsonResponse({
            "id": vet.id,
            "name": vet.name,
            "specialization": vet.specialization,
            "image": vet.image.url if vet.image else None  
        })

    return HttpResponse('This is a POST only endpoint!', status=405)

def return_all_vets(request):
    vets =  Vets.objects.all()
   

    vets_serialized = []

    for vet in vets:
        vets_serialized.append({
           "id":vet.id,
           "name":vet.name,
           "specialization":vet.specialization,
           "image":vet.image.url
           
        })


    print(vets_serialized)
    return JsonResponse(vets_serialized, safe = False)

def return_all_pets(request):
    pets =  Pets.objects.all()
   

    pets_serialized = []

    for pet in pets:
        pets_serialized.append({
           "id":pet.id,
           "name":pet.name,
           "species":pet.species,
           "age":pet.age,
           "owner_id":pet.owner.id,
           "image":pet.image.url
           
        })


    print(pets_serialized)
    return JsonResponse(pets_serialized, safe = False)

def create_pet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        age = request.POST.get('age')
        owner_id = request.POST.get('owner_id')
        image = request.FILES.get('image')  

        pet = Pets.objects.create(
            name=name,
            species=species,
            age=age,
            owner_id=owner_id,
            image=image
        )

        return JsonResponse({
            "id": pet.id,
            "name": pet.name,
            "species": pet.species,
            "age": pet.age,
            "owner_id": pet.owner_id,
            "image": pet.image.url if pet.image else None  
        })

    return HttpResponse('This is a POST only endpoint!', status=405)
    

def delete_pet(request, pet_id):
    if request.method == 'DELETE':
        pet = get_object_or_404(Pets, pk = pet_id)

        pet.delete()
        return HttpResponse(f'Pet with id: {pet_id} was deleted', status = 200)

    else:
        return HttpResponse('This is a DELETE only endpoint!', status = 405)
    


def update_pet(request, pet_id):
    if request.method != 'PUT':
        return HttpResponseNotAllowed(['PUT'])

    # Manually read the body and parse it as multipart
    # Required because Django only parses multipart for POST
    if 'multipart/form-data' in request.content_type:
        # Need to manually parse the body
        from django.http.multipartparser import MultiPartParser, MultiPartParserError

        try:
            parser = MultiPartParser(request.META, request, request.upload_handlers)
            data, files = parser.parse()
        except MultiPartParserError as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Unsupported content type'}, status=400)

    pet = get_object_or_404(Pets, pk=pet_id)

    pet.name = data.get('name', pet.name)
    pet.species = data.get('species', pet.species)
    pet.age = data.get('age', pet.age)
    pet.owner_id = data.get('owner_id', pet.owner_id)

    if 'image' in files:
        pet.image = files['image']

    pet.save()

    return JsonResponse({
        "id": pet.id,
        "name": pet.name,
        "species": pet.species,
        "age": pet.age,
        "owner_id": pet.owner_id,
        "image": pet.image.url if pet.image else None,
    })



def update_owner(request, owner_id):
    if request.method == 'PATCH':
        owner = get_object_or_404(Owners, pk = owner_id)
        data = json.loads(request.body)

        if 'name' in data:
            owner.name = data['name']

        if 'phone' in data:
            owner.phone = data['phone']

        owner.save()

        return JsonResponse({
            "id":owner.id,
            "name":owner.name,
            "phone":owner.phone
        })
    else:
        return HttpResponse('This is a PATCH only endpoint!', status = 405)


def delete_owner(request, owner_id):
    if request.method == 'DELETE':
        owner = get_object_or_404(Owners, pk = owner_id)

        owner.delete()
        return HttpResponse(f'Owner with id: {owner_id} was deleted', status = 200)

    else:
        return HttpResponse('This is a DELETE only endpoint!', status = 405)


    
def create_owner(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        owner = Owners.objects.create(
            name = data['name'],
            phone = data['phone']
        )
        return JsonResponse({
            "id":owner.id,
            "name":owner.name,
            "phone":owner.phone
        })
    else:
        return HttpResponse('This is a POST only endpoint!', status = 405)

def return_all_pets_by_owner(request, owner_id):
    owner = get_object_or_404(Owners, pk=owner_id)

    pets = Pets.objects.filter(owner = owner) #pet owner = owner declared up top in method

    
    pets_serialized = []

    for pet in pets:
        pets_serialized.append({
           "id":pet.id,
           "name":pet.name,
           "species":pet.species,
           "age":pet.age,
           "image":pet.image
        })

    return JsonResponse({
        "owner_id":owner.id,
        "owner_name":owner.name,
        "owner_phone":owner.phone,
        "pets":pets_serialized
    })



def return_all_owners(request):
    owners = Owners.objects.all()
   

    owners_serialized = []

    for owner in owners:
        owners_serialized.append({
           "id":owner.id,
           "name":owner.name,
           "phone":owner.phone
        })


    print(owners_serialized)
    return JsonResponse(owners_serialized, safe = False)


def simple_test(request):
    return HttpResponse('This is the test page')


def simple_test_post(request):
    if request.method == 'POST':
        decoded_data = request.body.decode('utf-8')
        print(decoded_data)
        return HttpResponse('Data was recieved!')
    else:
        return HttpResponse('This is a POST only endpoint!', status=405)