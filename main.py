from fastapi import FastAPI, HTTPException
from mongoengine import connect
import pendulum
from typing import List


from models.airlinemodel import Airlines
from models.airportmodel import Airports
from models.basemodels.MultiFlightRecommendationRequest import MultiFlightRecommendationRequest
from models.basemodels.multicityflightrecommendationresponse import MultiFlightRecommendationResponse
from models.routemodel import RoutesData
from models.basemodels.recommendationrequest import RecommendationRequest
from models.basemodels.multifilterrequest import MultiFilterRequest
from models.basemodels.recommendationresponse import RecommendationResponse
from models.basemodels.airlineresponse import AirlinesResponse
from models.basemodels.airportsresponse import AirportsResponse
from models.basemodels.autocompletemodelresponse import AirportAutoResponse
from models.basemodels.AirportAutoRequest import AirportAutoRequest
from models.basemodels.detailed_itinerary import ItineraryRequest, ItineraryResponse
from models.basemodels.recommend import Recommend
app = FastAPI()


@app.get("/airlines/all", response_model=List[AirlinesResponse])
async def get_all_airlines():
    airlines = Airlines.objects.all()
    return [AirlinesResponse(**airline.to_mongo()) for airline in airlines]


@app.get("/airlines/{airline_id}", response_model=AirlinesResponse)
async def read_airline(airline_id: str):
    try:
        airline = Airlines.objects.get(id=airline_id)
        return AirlinesResponse(**airline.to_mongo())
    except Airlines.DoesNotExist:
        raise HTTPException(status_code=404, detail="Airline not found")


@app.get("/airlines/by-code/{airline_code}", response_model=AirlinesResponse)
async def get_airline_by_code(airline_code: str):
    try:
        airline = Airlines.objects.get(code=airline_code)
        return AirlinesResponse(**airline.to_mongo())
    except Airlines.DoesNotExist:
        raise HTTPException(status_code=404, detail="Airline not found")


@app.get("/airports/all", response_model=List[AirportsResponse])
async def get_all_airports():
    airports = Airports.objects.all()
    return [AirportsResponse(**airport.to_mongo()) for airport in airports]


@app.get("/airports/by-code/{airport_code}", response_model=AirportsResponse)
async def get_airport_by_code(airport_code: str):
    try:
        airport = Airports.objects.get(code=airport_code)
        return AirportsResponse(**airport.to_mongo())
    except Airports.DoesNotExist:
        raise HTTPException(status_code=404, detail="Airport not found")


# @app.post("/airports/by-code", response_model=AirportsResponse)
# async def get_airport_by_codes(airport_code: str):
#     try:
#         airport = Airports.objects.get(code=airport_code)
#         return AirportsResponse(**airport.to_mongo())
#     except Airports.DoesNotExist:
#         raise HTTPException(status_code=404, detail="Airport not found")


@app.get("/airports/{airport_id}", response_model=AirportsResponse)
async def get_airport(airport_id: str):
    try:
        airport = Airports.objects.get(id=airport_id)
        return AirportsResponse(**airport.to_mongo())
    except Airports.DoesNotExist:
        raise HTTPException(status_code=404, detail="Airport not found")


@app.post("/recommendations", response_model=List[RecommendationResponse])
async def get_recommendations(request_data: RecommendationRequest):
    try:
        pendulum_datetime = pendulum.parse(request_data.dateoftravel)

        weekday_number = pendulum_datetime.weekday()

        weekday_to_day = {
            0: "day1",
            1: "day2",
            2: "day3",
            3: "day4",
            4: "day5",
            5: "day6",
            6: "day7",
        }

        day_field = weekday_to_day.get(weekday_number)

        routes = RoutesData.objects(
            iata_from=request_data.iatafrom,
            iata_to=request_data.iatato,
            **{day_field: "yes"},
            class_business=request_data.class_business,
            class_economy=request_data.class_economy,
            class_first=request_data.class_first
        )
        recommendations = []
        for route in routes:
            recommendations.append(RecommendationResponse(
                common_duration=route.common_duration,
                min_duration=route.min_duration,
                max_duration=route.max_duration,
                flights_per_day=route.flights_per_day,
                flights_per_week=route.flights_per_week,
                airline_name=route.airline_name,
                airline_code=route.airline_code,
                day1=route.day1,
                day2=route.day2,
                day3=route.day3,
                day4=route.day4,
                day5=route.day5,
                day6=route.day6,
                day7=route.day7,
                iata_from=route.iata_from,
                iata_to=route.iata_to,
                class_business=route.class_business,
                class_economy=route.class_economy,
                class_first=route.class_first,
                is_scheduled_passenger=route.is_scheduled_passenger,
                is_cargo=route.is_cargo
            ))
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/multi_filter_recommendation", response_model=List[RecommendationResponse])
async def get_multi_recommendations(request_data: MultiFilterRequest):
    try:
        filter_dict = {
            "airline_code__in": request_data.airline_codes,
        }

        if request_data.class_business == 1:
            filter_dict["class_business"] = 1
        if request_data.class_economy == 1:
            filter_dict["class_economy"] = 1
        if request_data.class_first == 1:
            filter_dict["class_first"] = 1

        routes = RoutesData.objects(**filter_dict)

        recommendations = []
        for route in routes:
            recommendations.append(RecommendationResponse(
                common_duration=route.common_duration,
                min_duration=route.min_duration,
                max_duration=route.max_duration,
                flights_per_day=route.flights_per_day,
                flights_per_week=route.flights_per_week,
                airline_name=route.airline_name,
                airline_code=route.airline_code,
                day1=route.day1,
                day2=route.day2,
                day3=route.day3,
                day4=route.day4,
                day5=route.day5,
                day6=route.day6,
                day7=route.day7,
                iata_from=route.iata_from,
                iata_to=route.iata_to,
                class_business=route.class_business,
                class_economy=route.class_economy,
                class_first=route.class_first,
                is_scheduled_passenger=route.is_scheduled_passenger,
                is_cargo=route.is_cargo
            ))
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/multi_city_flight_recommendation", response_model=List[MultiFlightRecommendationResponse])
async def get_multi_recommendations(request_data: MultiFlightRecommendationRequest):
    try:
        weekday_to_day = {
            0: "day1",
            1: "day2",
            2: "day3",
            3: "day4",
            4: "day5",
            5: "day6",
            6: "day7",
        }

        classess = {
            0: "BUS",
            1: "ECO",
            2: "FIRST"
        }

        filter_dict = {

        }

        if request_data.airlines:
            filter_dict["airline_code__in"] = request_data.airlines

        if request_data.classfields is not None:
            if "BUS".lower() in [item.lower() for item in request_data.classfields]:
                filter_dict["class_business"] = 1

            if "ECO".lower() in [item.lower() for item in request_data.classfields]:
                filter_dict["class_economy"] = 1

            if "FIRST".lower() in [item.lower() for item in request_data.classfields]:
                filter_dict["class_first"] = 1

        recommendations = []

        for dateItem in request_data.routes:
            pendulum_datetime = pendulum.parse(dateItem.date)
            weekday_number = pendulum_datetime.weekday()
            day_field = weekday_to_day.get(weekday_number)
            existing_route = RoutesData.objects(
                **{day_field: "yes"},
                iata_from=dateItem.departure,
                iata_to=dateItem.arrival,
                **filter_dict
            )

            resultroute = []

            for routedataItem in existing_route:
                resultroute.append(Recommend(
                    uid=routedataItem.uid,
                    common_duration=routedataItem.common_duration,
                    min_duration=routedataItem.min_duration,
                    max_duration=routedataItem.max_duration,
                    flights_per_day=routedataItem.flights_per_day,
                    flights_per_week=routedataItem.flights_per_week,
                    airline_name=routedataItem.airline_name,
                    airline_code=routedataItem.airline_code,
                    day1=routedataItem.day1,
                    day2=routedataItem.day2,
                    day3=routedataItem.day3,
                    day4=routedataItem.day4,
                    day5=routedataItem.day5,
                    day6=routedataItem.day6,
                    day7=routedataItem.day7,
                    airport_from=routedataItem.airport_from,
                    airport_to=routedataItem.airport_to,
                    iata_from=routedataItem.iata_from,
                    iata_to=routedataItem.iata_to,
                    class_business=routedataItem.class_business,
                    class_economy=routedataItem.class_economy,
                    class_first=routedataItem.class_first,
                    is_scheduled_passenger=routedataItem.is_scheduled_passenger,
                    is_cargo=routedataItem.is_cargo
                ))
            recommendations.append({
                "date": dateItem.date,
                "departure": dateItem.departure,
                "arrival": dateItem.arrival,
                "results": resultroute
            })
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/airport/autocomplete", response_model=List[AirportAutoResponse])
async def airport_autocomplete(request_data: AirportAutoRequest):
    try:
        matching_airports = Airports.objects(name__iregex=f".*{request_data.search_string}.*")[:request_data.limit]

        if not matching_airports:
            raise HTTPException(status_code=404, detail="No matching airports found.")

        return [{"code": airport.code, "name": airport.name} for airport in matching_airports]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/get_detailed_itinerary", response_model=List[ItineraryResponse])
async def get_detailed_itinerary(request_data: ItineraryRequest):
    try:
        filter_dict = {
            "uid__in": request_data.routes,
        }
        routes = RoutesData.objects(**filter_dict)

        itinerary_details = []
        for route in routes:
            itinerary_details.append(ItineraryResponse(
                id=route.uid,
                flying_from={
                    "name": route.airport_from,
                    "code": route.iata_from
                },
                flying_to={
                    "name": route.airport_to,
                    "code": route.iata_to
                },
                airline={
                    "name": route.airline_name,
                    "code": route.airline_code
                }
            ))
        return itinerary_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    connect(host="mongodb+srv://amal:Vv14t8Ig7MukqL5R@cluster0.x4j0e.mongodb.net/flight-routes")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
