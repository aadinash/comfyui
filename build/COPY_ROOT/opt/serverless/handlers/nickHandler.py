from handlers.basehandler import BaseHandler

def extract_filename(url):
    return url.split('/')[-1]

class NickWorkflow(BaseHandler):

    WORKFLOW_JSON = "/opt/serverless/workflows/nickWorkflow.json"

    def __init__(self, payload):
        super().__init__(payload, self.WORKFLOW_JSON)
        self.apply_modifiers()

    # verify this, but I think that it only auto-downloads the link when I modify the workflow
    def apply_modifiers(self):
        gender = self.get_value("gender", "male")
        mannequin = self.get_value("mannequin", "https://i.ibb.co/w6TSgng/m-short5.png")

        high_weight_links = [
            "https://i.ibb.co/w6TSgng/m-short5.png",
            "https://i.ibb.co/vLxSkb4/m-tall5.png",
            "https://i.ibb.co/qmV2YqM/m-short6.png",
            "https://i.ibb.co/G2SsD0r/m-tall6.png",
            "https://i.ibb.co/q98dyL7/f-tall5.png",
            "https://i.ibb.co/w6TSgng/m-short5.png",
            "https://i.ibb.co/qdKQvzT/f-tall6.png",
            "https://i.ibb.co/1mVcBKV/f-short6.png"
        ]

        weight_classification = "high" if mannequin in high_weight_links else "low"

        self.prompt["prompt"]["52"]["inputs"]["image"] = extract_filename(mannequin)

        # going to have to edit the js to choose these categories
        if gender.lower() == "male" and weight_classification == "high":
            self.prompt["prompt"]["6"]["inputs"]["text"] = "full body photo of a very heavy man wearing a vibrant wavy sweater, straight-leg blue pants, plus size, face details, grey studio background"
        elif gender.lower() == "male" and weight_classification == "low":
            self.prompt["prompt"]["6"]["inputs"]["text"] = "full body photo of a man wearing a vibrant wavy sweater, straight-leg blue pants, face details, grey studio background"
        elif gender.lower() == "female" and weight_classification == "high":
            self.prompt["prompt"]["6"]["inputs"]["text"] = "full body photo of a very heavy woman wearing a vibrant wavy sweater, straight-leg blue pants, plus size, face details, grey studio background"
        elif gender.lower() == "female" and weight_classification == "low":
            self.prompt["prompt"]["6"]["inputs"]["text"] = "full body photo of a woman wearing a vibrant wavy sweater, straight-leg blue pants, face details, grey studio background"
        else:
            self.prompt["prompt"]["6"]["inputs"]["text"] = "full body photo of a person wearing a vibrant wavy sweater, straight-leg blue pants, face details, grey studio background"

        if gender.lower() == "male":
            self.prompt["propmt"]["17"]["inputs"]["text"] = "photo of a man, skin details"
        else: 
            self.prompt["propmt"]["17"]["inputs"]["text"] = "photo of a woman, skin details"

        self.prompt["prompt"]["72"]["inputs"]["image"] = self.get_value("base64string", "")


"""
Example Request Body:

{
    "input": {
        "handler": "NickWorkflow",
        "webhook_extra_params": {},
        "mannequin": "some-link.url",
        "gender": "male",
        "base64string": "somesuperlongstringwithalotofstuffinit"
    }
}

"""
