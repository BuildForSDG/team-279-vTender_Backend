from app import api, app
from app.resources import Index
from app.resources.auth import UserLogin, UserRegister
from app.resources.tenders import TenderListAPI, TenderAPI
from app.resources.company import CompanyListAPI, CompanyAPI

""" Defining the API endpoints """
api.add_resource(Index, "")
api.add_resource(UserRegister, "/auth/register")
api.add_resource(UserLogin, "/auth/login")
api.add_resource(TenderListAPI, "/tenders")
api.add_resource(TenderAPI, "/tenders/<string:tender_id>")
api.add_resource(CompanyListAPI, "/company")
api.add_resource(CompanyAPI, "/company/<string:company_id>")


if __name__ == "__main__":
    app.run()
