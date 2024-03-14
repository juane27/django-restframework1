from django.http import HttpResponse
from rest_framework.decorators import api_view
from e_commerce.models import Comic, WishList
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)




@api_view(['GET'])
def hello_world(request):
    template = '<h1>Hello world Django APIs!</h1>' 
    return HttpResponse(template)


@api_view(['GET'])
def comic_list_api_view(request):
    if request.method == 'GET':

        _queryset = Comic.objects.all()
        print('holaaaaaa')
        print(_queryset)

        _data = list(_queryset.values()) if _queryset.exists() else []
        if _queryset.exists():
            # comic_data = _queryset() 

        # return JsonResponse(data=_data, safe=False, status=200)
            return render(request, 'comic_list.html', {'comic_data': _data})
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )

@api_view(['GET'])
def comic_list_api_view_by_id(request, marvel_id):
    logger.debug('Este es el marvel id: %s' % marvel_id)
    print('este es el marvel id', marvel_id)
    
    if request.method == 'GET':
        _queryset = Comic.objects.filter(marvel_id=marvel_id)
        _data = list(_queryset.values()) if _queryset.exists() else []
        
        if _queryset.exists():
            comic_data = _queryset.first()  # Obtén el primer cómic (puedes ajustar según tu lógica)
            return render(request, 'comic_details.html', {'comic_data': comic_data})
        else:
            return render(request, 'comic_details.html', {'marvel_id': marvel_id})
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )



@api_view(['GET'])
def comic_list_filtered_api_view(request):
    
    if request.method == 'GET':
        _queryset = Comic.objects.filter( price__gte=5.00)
        _data = list(_queryset.values()) if _queryset.exists() else []
        
        print(_queryset)
        if _queryset.exists():
            filtro_comic = 1
            comic_data = _queryset  
            return render(request, 'comic_list.html', {'comic_data': comic_data, 'filtro_comic': filtro_comic})
        else:
            filtro_comic = 0
            return render(request, 'comic_list.html', {'filtro_comic': filtro_comic})
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )
    


@api_view(['GET'])
def comic_list_filtered_api_view_stock(request):
    
    if request.method == 'GET':
        _queryset = Comic.objects.filter( stock_qty__gte=10)
        _data = list(_queryset.values()) if _queryset.exists() else []
        
        print(_queryset)
        if _queryset.exists():
            filtro_comic = 2
            comic_data = _queryset  
            return render(request, 'comic_list.html', {'comic_data': comic_data, 'filtro_comic': filtro_comic})
        else:
            filtro_comic = 3
            return render(request, 'comic_list.html', {'filtro_comic': filtro_comic})
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )




@api_view(['GET','POST'])
def comic_create_api_view(request):
    if request.method == 'GET':

        return render(request, 'comic_create.html')
    


    
    elif request.method == 'POST':
            
            _request = dict(request.POST)
            _marvel_id = _request.pop('marvel_id', None)
            titulo = _request.pop('titulo', None)
            cantidad = _request.pop('cantidad', None)
            precio = _request.pop('precio', None)
            descripcion = _request.pop('descripcion', None)
            picture = _request.pop('picture', None)

            if not _marvel_id:
                return JsonResponse(
                    data={"marvel_id": "Este campo no puede ser nulo."},
                    status=400
            )

            try:
                _instance, _created = Comic.objects.get_or_create(
                    marvel_id=_marvel_id[0],
                    title=titulo[0],
                    stock_qty= cantidad[0],
                    price = precio[0],
                    description = descripcion[0],
                    picture = picture[0]
                )


                if _created:
                    return JsonResponse(
                        data=_request(_instance), status=201
                    )
        
            except:
                return JsonResponse(
                    data={
                        "marvel_id": "Ya existe un comic con ese valor, debe ser único."
                    },
                    status=400
                )





        
            
            # # Guardar los datos en la base de datos
            # # ...

            # return render(request, 'comic_create.html', {'mensaje': 'Comic creado exitosamente'}, status=201)
    

