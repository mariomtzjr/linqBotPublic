def cacre(row):

    xml = """
        <movimiento>
            <tipoop>CACRE</tipoop>
            <contrato>{}</contrato>
            <anexo>N</anexo>
            <nuacreedor>{}</nuacreedor>
        </movimiento>
    """.format(row[30], row[31])

    return xml
