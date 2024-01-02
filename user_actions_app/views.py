from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserAction

@csrf_exempt
def record_user_action(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_action = UserAction.objects.create(
                product_id=data['product_id'],
                action_type=data['action_type'],
                action_datetime=data['action_datetime'],
                user_id=data['user_id'],
                # Add more fields here if needed based on your model
            )
            return JsonResponse({'message': 'User action recorded successfully!'})
        except KeyError as e:
            return JsonResponse({'error': f'Missing key: {e}'}, status=400)
        except ValueError as e:
            return JsonResponse({'error': f'Invalid value: {e}'}, status=400)
        except UserAction.DoesNotExist:
            return JsonResponse({'error': 'UserAction does not exist'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
