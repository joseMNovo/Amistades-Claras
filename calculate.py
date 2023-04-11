def calcular(amistades):
    print(f"amistades in calculate: {amistades}")

    amistades = {amistades[i+1]: int(amistades[i]) for i in range(0, len(amistades), 2)}

    total = [amistades[a] for a in amistades]
    total_a_pagar = sum(total) / len(total)
    total_a_pagar = round(total_a_pagar, 2)
    total_a_pagar_sindos = round(total_a_pagar)

    amistades_claras = [f"Total por persona: {total_a_pagar} ({total_a_pagar_sindos})"]

    for amistad, puso in amistades.items():
        if puso < total_a_pagar:
            amistades_claras.append(f"{amistad} debe {round(total_a_pagar - puso, 2)}")
            #print(f"{amistad} debe {round(total_a_pagar - puso, 2)}")

        elif puso > total_a_pagar:
            amistades_claras.append(f"A {amistad} le deben {round(puso - total_a_pagar, 2)}")
            #print(f"A {amistad} le deben {round(puso - total_a_pagar, 2)}")

    print(f"amistades_claras in calculate: {amistades_claras}")
    return amistades_claras


