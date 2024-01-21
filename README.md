# Backend Clarke Energia

### Tecnologias utilizadas:

- Python;
- Flask;
- Cyclic;
- MySQL Connector.

---

### Banco de dados:

- **MySQL** hospedado na **Azure**
- Modelo lógico:

![](./database/dbclarkeenergia.png)

---
### EndPoints:

Hospedado em `https://clarkeenergia.cyclic.app/`

**GET** (todos os fornecedores)
```py
/providers
```

**GET** (filtro de fornecedores por kwh mínimo)
```py
/providers?minimum_kwh={kwh}
```

---
### Autora

- [Yasmin Gonçalves](https://github.com/yasmingcv)
