from django.http import HttpResponse
from products.models import Product, Device
from django.core import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from products.models import Reading
import logging


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def route_readings_requests_GET_POST(request, pid, id):
    match request.method:
        case "GET":
            return get_readings(request, pid, id)
        case "POST":
            return create_readings(request, pid, id)


def get_readings(request, pid, id):
    """
    Description: This API gets all readings within a start and end time range in milliseconds.
    parameters:
    - name: start
        type: int
        required: true
    - name: end
        type: int
        required: true
    """
    products = Product.objects.all()
    start = request.query_params.get("start")
    end = request.query_params.get("end")
    print(f"Start: {start}")
    print(f"End: {end}")

    return HttpResponse(
        serializers.serialize("json", products), content_type="application/json"
    )


def create_readings(request, pid, id):
    """
    Description: This API imports readings.
    """
    try:
        csv_file = request.FILES["readings"]
        if not csv_file.name.endswith(".csv"):
            return HttpResponse("Bad request: File is not CSV type.", status=400)
        if csv_file.multiple_chunks():
            return HttpResponse(
                "Bad request: Uploaded file is too big (%.2f MB)."
                % (csv_file.size / (1000 * 1000),),
                status=400,
            )
        file_data = csv_file.read().decode("utf-8")
        try:
            device = Device.objects.get(id=id)
            lines = file_data.split("\n")
            for line in lines:
                if line:
                    fields = line.split(",")
                    if fields:
                        Reading.objects.create(
                            timestamp=fields[0],
                            device=device,
                            ppm_co2_water=fields[1],
                            ppm_co2_air=fields[2],
                            water_temp=fields[3],
                        )
        except Device.DoesNotExist:
            device = None
            return HttpResponse("Bad request: Device not found.", status=400)

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        return HttpResponse("Bad request: Unable to upload file.", status=400)
    return HttpResponse("Created.", status=201)
