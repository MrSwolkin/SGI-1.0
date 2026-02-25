# Modelos de Dados

## Diagrama de Relacionamentos

```
USER ||--o{ TRANSACTION : "realiza"
ASSET ||--o{ TRANSACTION : "referenciado em"
USER ||--o| PORTFOLIO : "possui"
```

## Models

### User (CustomUser)

Extende `AbstractUser` do Django. Login por email (nao username).

| Campo | Tipo | Restricao |
|---|---|---|
| id | int | PK |
| email | EmailField | unique |
| first_name | CharField | obrigatorio |
| last_name | CharField | obrigatorio |
| password | CharField | hashed pelo Django |
| is_active | BooleanField | default True |
| date_joined | DateTimeField | auto |

- `USERNAME_FIELD = 'email'`
- `REQUIRED_FIELDS = ['first_name', 'last_name']`

### Asset

Ativo financeiro (acao, FII, ETF, stock internacional).

| Campo | Tipo | Restricao |
|---|---|---|
| id | int | PK |
| ticker | CharField | unique |
| name | CharField | — |
| asset_type | CharField | choices: STOCK, FII, ETF, INTERNATIONAL |
| currency | CharField | choices: BRL, USD |
| created_at | DateTimeField | auto_now_add |
| updated_at | DateTimeField | auto_now |

### Transaction

Operacao de compra ou venda de um ativo.

| Campo | Tipo | Restricao |
|---|---|---|
| id | int | PK |
| user | ForeignKey | → User |
| asset | ForeignKey | → Asset |
| transaction_type | CharField | choices: BUY, SELL |
| quantity | DecimalField | — |
| unit_price | DecimalField | — |
| fee | DecimalField | default 0 |
| operation_date | DateField | — |
| created_at | DateTimeField | auto_now_add |
| updated_at | DateTimeField | auto_now |

**Propriedade calculada**: `total_value = quantity * unit_price + fee`

### Portfolio

Vinculo 1-para-1 entre usuario e sua carteira.

| Campo | Tipo | Restricao |
|---|---|---|
| id | int | PK |
| user | OneToOneField | → User |
| created_at | DateTimeField | auto_now_add |
| updated_at | DateTimeField | auto_now |

O portfolio nao armazena valores. Todos os calculos (total investido, composicao, preco medio) sao feitos dinamicamente a partir das transacoes do usuario.
