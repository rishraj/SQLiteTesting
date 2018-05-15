from py2neo import Graph, Node, Relationship, authenticate

authenticate("localhost:7474", "neo4j", "123")
graph = Graph()

graph.delete_all()

term_attr = {"Start Date": 0, "End Date": 0, "Delivery Date": 0, "Effective Date": 0}
term = Node("Term", **term_attr, name="Term")
graph.create(term)

landlord_attr = {'Address': 0, 'Notice Address': 0, 'Rights': 0, 'Audit Rights': 0}
landlord = Node("Landlord", **landlord_attr, name="Landlord")
graph.create(landlord)

rent_attr = {'Percentage Rental': 0, 'Minimum Annual Rental': 0, 'MAR Increase Percentage': 0, 'Additional Rent': 0, 'Late Charge': 0, 'Late Opening Fee': 0}
rent = Node("Rent", **rent_attr, name="Rent")
graph.create(rent)

tax_attr = {'Administration Fee': 0, 'Per sq. Foot': 0}
tax = Node("Tax", **tax_attr, name="Tax")
graph.create(tax)

broker_attr = {'Commission': 0}
broker = Node("Broker", **broker_attr, name="Broker")
graph.create(broker)

# graph.create(Relationship(commission, broker))

tenant_attr = {'Notice Address': 0, 'Sign': 0}
tenant = Node("Tenant", **tenant_attr, name="Tenant")
graph.create(tenant)

governing_law = Node("Governing Law", name="Governing Law")
graph.create(governing_law)

tenant_insurance_attr = {'Commercial General Liability': 0, 'Injury/Death/Property/Auto Liability': 0, 'Workend Compensation Coverage': 0, 'Product Liability Coverage': 0}
tenant_insurance = Node("Tenant Insurance", **tenant_insurance_attr, name="Tenant Insurance")
graph.create(tenant_insurance)

other_charges_attr = {"Trash Removal": 0,"Parking Validation": 0,"Common Area": 0, "Common Area HVAC": 0,
                     "Promotional Program/Intial Assessment": 0}
other_charges = Node("Value", **other_charges_attr, name = "other charges")
graph.create(other_charges)


utility_attr = {"Water & Sewer": 0,"Fire Detection": 0,"Electric": 0}
utility_charges = Node("Value", **utility_attr, name = "Utility Charges")
graph.create(utility_charges)

deposits_attr = {"Security": 0, "Lease": 0, "Letter Of Credit": 0}
deposits = Node("Value", **deposits_attr, name="Deposits")
graph.create(deposits)

design_charges_attr = {"Admin Services": 0, "Construction Deposit": 0, "Construction Barricade": 0, "Barricade Graphic Charge": 0, "Design Fee": 0}
design = Node("Value", **design_charges_attr, name="Design Charges")
graph.create(design)

landlord_insurance_attr = {"Comprehensive Auto Liability Insurance": 0, "Tenant Protective Liability Insurance": 0, "Tenant Builder Risk Insurance": 0}
landlord_insurance = Node("Value", **landlord_insurance_attr, name="Landlord Insurance")
graph.create(landlord_insurance)

rented_attr = {"Area": 0,"Number": 0}
rented = Node("Value", **rented_attr, name="Rented Floor")
graph.create(rented)

property_attr = {"Address": 0, "Area": 0, "Name": 0, "Permitted Use": 0, "Radius Area": 0}
property_ = Node("Value", **property_attr, name="Property")
graph.create(property_)


contract = Node("Contract", name="Contract")
graph.create(contract)

graph.create(Relationship(contract, term))
graph.create(Relationship(contract, landlord))
graph.create(Relationship(contract, rent))
graph.create(Relationship(contract, tax))
graph.create(Relationship(contract, broker))
graph.create(Relationship(contract, tenant))
graph.create(Relationship(contract, governing_law))
graph.create(Relationship(contract, tenant_insurance))
graph.create(Relationship(contract, other_charges))
graph.create(Relationship(contract, utility_charges))
graph.create(Relationship(contract, deposits))
graph.create(Relationship(contract, design))
graph.create(Relationship(contract, landlord_insurance))
graph.create(Relationship(contract, rented))
graph.create(Relationship(contract, property_))
