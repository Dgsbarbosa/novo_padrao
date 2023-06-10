from .models import Materials, Services

def total_services(id):
    
    services = Services.objects.filter(id_budget = id)
    
    values = []
    
    for service in services:
        value = service.total
        value = value.replace("R$","").replace(".","").replace(",",".")
        value = float(value)
        values.append(value)
        
    #     print("sevice.total:",service.total)
    
    # print('values:', sum(values))
    
    return sum(values)

def total_materials(id):
    materials = Materials.objects.filter(id_budget = id)
    
    values = []
    
    for material in materials:
        value = material.total
        value = value.replace("R$","").replace(".","").replace(",",".")
        value = float(value)
        values.append(value)
        
    
    return sum(values)