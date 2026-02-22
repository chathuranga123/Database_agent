from fastapi import APIRouter

from models import UserCreate, InvoiceCreate
import invoice_repository as repo

router= APIRouter(prefix="/invoices",tags=["invoices"])


@router.post("/")
def create_invoice(invoice:InvoiceCreate):
    result= repo.create_invoice(invoice.user_id,invoice.amount,invoice.description)
    return {
        "user_id":result[0],
        "amount":result[1],
        "description":result[2]
    }

@router.post("/{invoice_id}")
def get_invoice(invoice_id:int):
    result= repo.get_invoicer(invoice_id)
    return {
        "user_id": result[0],
        "amount": result[1],
        "description": result[2]
    }

@router.get("/")
def get_invoices():
    invoices = repo.get_invoices()
    invoices_list = []

    for invoice in invoices:
        invoices_list.append(
            {
                "id": invoice[0],
                "user_id": invoice[1],
                "amount": invoice[2],
                "description": invoice[3]
            }
        )
    return invoices_list

@router.delete("/{invoice_id}")
def delete_user(invoice_id: int):
    repo.delete_invoices(invoice_id)
    return {"response" : "Invoice Deleted Successfully"}




