# Pre-entrega 2: Pipeline de Procesamiento Validado con LCEL

Este repositorio contiene un **Pipeline de Extracción de Entidades Técnicas** asíncrono desarrollado con **LangChain Expression Language (LCEL)**, validación estricta con **Pydantic** y resiliencia automatizada mediante **`.with_retry()`**.

## 🏗️ Estructura del Pipeline

La composición del flujo sigue la sintaxis declarativa de LCEL:

```text
prompt | model.with_structured_output(ExtraccionTecnica).with_retry()