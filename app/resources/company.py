from flask import request
from flask_restful import Resource, reqparse, marshal
from app.resources import create_or_update_resource, delete_resource
from app.models import Company, TenderSchema, CompanySchema
from app.serializers import company_serializer

# init schema
tender_schema = TenderSchema()
tenders_schema = TenderSchema(many=True)

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)


class CompanyListAPI(Resource):
    """View all company; add new company
    URL: /api/v1/company
    Request methods: POST, GET
    """

    def get(self):

        args = request.args.to_dict()
        page = int(args.get("page", 1))
        limit = int(args.get("limit", 20))
        kwargs = {}

        company = Company.query.filter_by(**kwargs).paginate(page=page, per_page=limit, error_out=False)
        page_count = company.pages
        has_next = company.has_next
        has_previous = company.has_prev
        if has_next:
            next_page = str(request.url_root) + "api/v1.0/company?" + \
                        "limit=" + str(limit) + "&page=" + str(page + 1)
        else:
            next_page = "None"
        if has_previous:
            previous_page = request.url_root + "api/v1.0/company?" + \
                            "limit=" + str(limit) + "&page=" + str(page - 1)
        else:
            previous_page = "None"
        company = company.items

        output = {"company": marshal(company, company_serializer),
                  "has_next": has_next,
                  "page_count": page_count,
                  "previous_page": previous_page,
                  "next_page": next_page
                  }

        if company:
            return output
        else:
            return {"error": "There are no registered company. "
                             "Add a new one and try again!"}, 404


    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("tenderNumber", required=True, help="Please enter a tender number for a company.")
        parser.add_argument("companyName", required=True, help="Please enter a company name.")
        parser.add_argument("directors", required=True, help="Please enter a directors.")
        parser.add_argument("companyRegistrationNo", required=True, help="Please enter a company registration number.")
        parser.add_argument("company_phone_number", help="Enter the company phone number.")
        parser.add_argument("companyAddress", help="Enter the company address.")
        parser.add_argument("awardedPoint", required=True, help="Please enter awarded point.")

        args = parser.parse_args()

        tenderNumber, companyName, directors, companyRegistrationNo, company_phone_number, companyAddress, awardedPoint = \
            args["tenderNumber"], args["companyName"], args["directors"], args["companyRegistrationNo"], \
            args["company_phone_number"], args["companyAddress"], args["awardedPoint"]

        company = Company(tenderNumber=tenderNumber,
                          companyName=companyName,
                          directors=directors,
                          companyRegistrationNo=companyRegistrationNo,
                          company_phone_number=company_phone_number,
                          companyAddress=companyAddress,
                          awardedPoint=awardedPoint
                          )
        # if company.apply_count == 'null' and companyRegistrationNo is not None:
        #     try:
        #         companyRegistrationNo = Company.query.get(companyRegistrationNo)
        #         if companyRegistrationNo:
        #             count += 1
        #             company.apply_count.append(count)
        #         else:
        #             return {"error": "cannot assign value to apply_count"}, 400
        #     except:
        #         return {"error": "The company already apply for this tender number"}, 400
        return create_or_update_resource(resource=company, resource_type="company", serializer=company_serializer, create=True)


class CompanyAPI(Resource):
    """View, update and delete a single company.
    URL: /api/v1/company/<company_id>
    Request methods: GET, PUT, DELETE
    """

    def get(self, company_id):

        company = Company.query.filter_by(company_id=company_id).first()
        if company:
            return marshal(company, company_serializer)
        else:
            return {"error": "A company with ID " + company_id + " does " "not exist."}, 404


    def put(self, company_id):
        company = Company.query.filter_by(company_id=company_id).first()
        if company:
            parser = reqparse.RequestParser()
            parser.add_argument("companyName")
            parser.add_argument("directors")
            parser.add_argument("companyRegistrationNo")
            parser.add_argument("company_phone_number")
            parser.add_argument("companyAddress")
            parser.add_argument("apply_count")
            parser.add_argument("winning_count")
            parser.add_argument("awardedPoint")
            args = parser.parse_args()
            for field in args:
                if args[field] is not None:
                    updated_field = args[field]
                    setattr(company, field, updated_field)
            return create_or_update_resource(resource=company, resource_type="company", serializer=company_serializer, create=False)
        else:
            return {"error": "A company with ID " + company_id + " does not exist."}, 404


    def delete(self, company_id):
        company = Company.query.filter_by(company_id=company_id).first()
        if company:
            return delete_resource(resource=company, resource_type="company", id=company_id)
        else:
            return {"error": "A company with ID " + company_id + " does " "not exist."}, 404
