from flask_restx import Namespace, fields  # type: ignore

router = Namespace("blazegraphModels", description="Models for database interaction")

query_model = router.model(
    "SelectQueryInDB",
    {
        "query": fields.String(
            example="SELECT ?class WHERE {?class a <http://src/rtw#Class>}",
            description="The query to be executed to retrieve data",
        ),
    },
)
