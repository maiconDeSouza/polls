# Projeto Enquete

Este é um projeto Django de uma aplicação de enquetes simples.

## Funcionalidades

- **Criação de Enquetes:**  
  Apenas usuários com permissão de staff (superusuários) podem criar enquetes.

- **Votação:**  
  Todos os usuários podem ver as enquetes e suas opções. Entretanto, apenas usuários autenticados podem votar e visualizar os resultados. Cada usuário pode votar apenas uma vez por enquete.

- **Cadastro de Usuários:**  
  Usuários comuns podem se cadastrar através de uma tela personalizada.

- **Página Inicial:**  
  Lista todas as enquetes em formato de lista. Se o usuário estiver logado, ele poderá votar e ver os resultados.

## Estrutura do Projeto

- `mypolls/` - Projeto Django.
- `polls/` - App que gerencia as enquetes.
- `accounts/` - App que gerencia o cadastro e autenticação dos usuários.

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/projeto-enquete.git
   cd projeto-enquete