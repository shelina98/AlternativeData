import time

import requests

X_Phantombuster_Key = "lGr15TFM0qNO4FppxrZUFMzTPJdYlhikYfdF20ufQ9g"


class PhantomService:

    @staticmethod
    def create_phantom_agent(linkedinUrl):
        url = "https://api.phantombuster.com/api/v2/agents/save?output=json"
        payload = {
            "org": "phantombuster",
            "script": "LinkedIn Companies Info.js",
            "branch": "master",
            "environment": "release",
            "argument": {"spreadsheetUrl": linkedinUrl}
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Phantombuster-Key": X_Phantombuster_Key
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        data = response.json()
        print(data["id"])
        return data["id"]

    @staticmethod
    async def call_phantom_agent(agentId, linkedinUrl):
        url = "https://api.phantombuster.com/api/v2/agents/launch"

        payload = {"id": agentId,
                   "argument": {"companiesPerLaunch": 250, "delayBetween": 2,
                                "sessionCookie": "AQEDAS445_QDDCUWAAABe5wPHFsAAAF-3hPwwU4AsiaSrybT74y29J8UQy7WoHoGj9Qg_35PQsEjx6EyWWnOkgEV69nMAU5G_3RSJIj0ZucyFzlhl3KIaynWwLCwtYvXKYPLnBrOJMouWH5JQxFVaQW0",
                                "spreadsheetUrl": linkedinUrl}}
        headers = {
            "Content-Type": "application/json",
            "X-Phantombuster-Key": X_Phantombuster_Key
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        data = response.json()
        print(data["containerId"])
        return data["containerId"]

    @staticmethod
    async def get_container_data(agentId, containerId, linkedinUrl):
        url = "https://api.phantombuster.com/api/v1/agent/" + str(agentId) + "/output?containerId=" + str(containerId)

        headers = {
            "Accept": "application/json",
            "X-Phantombuster-Key-1": X_Phantombuster_Key
        }
        payload = {"argument": {
            "sessionCookie": "AQEDAS445_QDDCUWAAABe5wPHFsAAAF-3hPwwU4AsiaSrybT74y29J8UQy7WoHoGj9Qg_35PQsEjx6EyWWnOkgEV69nMAU5G_3RSJIj0ZucyFzlhl3KIaynWwLCwtYvXKYPLnBrOJMouWH5JQxFVaQW0",
            "spreadsheetUrl": linkedinUrl}}

        response = requests.request("GET", url, json=payload, headers=headers)

        data = response.json()
        print(data["data"]["output"])
        return data["data"]["containerId"]

    @staticmethod
    def fetch(containerId):
        url = "https://api.phantombuster.com/api/v2/containers/fetch-output?id=" + str(containerId)

        headers = {
            "Accept": "application/json",
            "X-Phantombuster-Key": X_Phantombuster_Key
        }

        response = requests.request("GET", url, headers=headers)
        print(response.text)
