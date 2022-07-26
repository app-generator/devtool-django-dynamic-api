from django.http import Http404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from core.settings import DYNAMIC_API

from apps.models  import Utils 
from apps.helpers import check_permission

class DynamicAPI(APIView):

    # CREATE : POST api/model/
    #@method_decorator(login_required, name='dispatch')
    #@check_permission
    def post(self, request, **kwargs):
        try:
            model_serializer = Utils.get_serializer(DYNAMIC_API, kwargs.get('model_name'))(data=request.data)
            if model_serializer.is_valid():
                model_serializer.save()
            else:
                return Response(data={
                    **model_serializer.errors,
                    'success': False
                }, status=400)
        except KeyError:
            return Response(data={
                'message': 'this model is not activated or not exist.',
                'success': False
            }, status=400)
        return Response(data={
            'message': 'Record Created.',
            'success': True
        }, status=200)

    # READ : GET api/model/id or api/model
    def get(self, request, **kwargs):

        model_id = kwargs.get('id', None)
        try:
            if model_id is not None:

                # Validate for integer
                try:
                    model_id = int(model_id)

                    if model_id < 0:
                        raise ValueError('Expect positive int')

                except ValueError as e:
                    return Response(data={
                        'message': 'Input Error = ' + str(e),
                        'success': False
                    }, status=400)

                thing = get_object_or_404(Utils.get_manager(DYNAMIC_API, kwargs.get('model_name')), id=model_id)
                model_serializer = Utils.get_serializer(DYNAMIC_API, kwargs.get('model_name'))(instance=thing)
                output = model_serializer.data
            else:
                all_things = Utils.get_manager(DYNAMIC_API, kwargs.get('model_name')).all()
                thing_serializer = Utils.get_serializer(DYNAMIC_API, kwargs.get('model_name'))
                output = []
                for thing in all_things:
                    output.append(thing_serializer(instance=thing).data)
        except KeyError:
            return Response(data={
                'message': 'this model is not activated or not exist.',
                'success': False
            }, status=400)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=404)
        return Response(data={
            'data': output,
            'success': True
            }, status=200)

    # UPDATE : PUT api/model/id/
    #@method_decorator(login_required, name='dispatch')
    #@check_permission
    def put(self, request, **kwargs):
        try:
            thing = get_object_or_404(Utils.get_manager(DYNAMIC_API, kwargs.get('model_name')), id=kwargs.get('id'))
            model_serializer = Utils.get_serializer(DYNAMIC_API, kwargs.get('model_name'))(instance=thing,
                                                                                           data=request.data,
                                                                                           partial=True)
            if model_serializer.is_valid():
                model_serializer.save()
            else:
                return Response(data={
                    **model_serializer.errors,
                    'success': False
                }, status=400)
        except KeyError:
            return Response(data={
                'message': 'this model is not activated or not exist.',
                'success': False
            }, status=400)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=404)
        return Response(data={
            'message': 'Record Updated.',
            'success': True
            }, status=200)

    # DELETE : DELETE api/model/id/
    #@method_decorator(login_required, name='dispatch')
    #@check_permission
    def delete(self, request, **kwargs):
        try:
            model_manager = Utils.get_manager(DYNAMIC_API, kwargs.get('model_name'))
            to_delete_id = kwargs.get('id')
            model_manager.get(id=to_delete_id).delete()
        except KeyError:
            return Response(data={
                'message': 'this model is not activated or not exist.',
                'success': False
            }, status=400)
        except Utils.get_class(DYNAMIC_API, kwargs.get('model_name')).DoesNotExist as e:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=404)
        return Response(data={
            'message': 'Record Deleted.',
            'success': True
        }, status=200)
