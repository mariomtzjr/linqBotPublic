def saldo(row):
    xml = """
        <movimiento>
            <tipoop>SALDO</tipoop>
            <contrato>{}</contrato>
            <anexo>N</anexo>
            <numonto>{}</numonto>
        </movimiento>

    """.format(row[0], row[1])

    return xml
