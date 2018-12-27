
# import sys
# sys.path.append("/home/ruhil/Dropbox/projects/python3-SmartSchema/SmartSchema/SmartSchema")

from SmartSchema import SmartSchema


def reducedqty(inst):
    y = 0
    for x in inst["qty"]:
        y = y + x['qty']
    return y


if __name__ == "__main__":
    InvoiceSchema = {
        "type": "object",
        "required": [
            "reciver",
            "issuer",
            "inv_date"
        ],
        "properties": {
            "reciver": {
                "type": "string",
                "description": "uid of reciver"
            },
            "issuer": {
                "type": "string",
                "description": "uid of issuer"
            },
            "inv_date": {
                "type": "string",
                "description": "date of invoice",
                "accessor": lambda inst: "yolo",
            },
            "_id": {
                "type": "integer",
                "description": "ref_no for the invoice",
                "__comment__": "invoice in single series for now"
            },
            "txbl": {
                "type": "number",
                "description": "taxable amount",
                "accessor": lambda inst: inst['val'] * 100 / (100 + inst['tax']),
            },
            "tax": {
                "type": "number",
                "description": "tax rate",
                "accessor": lambda inst: (inst['val'] - inst['txbl']) / inst['txbl']
            },
            "net": {
                "type": "number",
                "description": "taxable + tax%",
                "accessor": lambda inst: inst['tax'] * inst['txbl'] / 100 + inst['txbl']
            },
            "qty": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "qty": {
                            "type": "number"
                        },
                        "half": {
                            "type": "number",
                        }
                    },
                    "required": ["qty"]
                }},
            "sumqty": {
                "type": "number",
                "description": "sum of qty",
                "accessor": reducedqty
            }
        }
    }

    schema = SmartSchema(InvoiceSchema)
    i = {
        "_id": 678,
        "issuer": "rke",
        "reciver": "@tfcgpl",
        # "tax": 18,
        "qty": [{"qty": 12}, {"qty": 13}],
        "txbl": 30000,
        "tax": 35400
    }
    schema.resolve(i)
    print(i)
    if not schema.validate(i):
        print("success: No issue found")
