
# 📝 CKAD Handbook - Preparação para o Certificado Kubernetes Developer (CKAD) By Aldry Albuquerque 🐳

Bem-vindo ao meu repositório de preparação para o exame **CKAD (Certified Kubernetes Application Developer)**! Aqui, registro tudo o que estou estudando e as práticas que estou realizando para garantir que estarei pronto para a prova.

## 🧭 Índice

1. [📖 Introdução](#-introdução)
2. [📂 Estrutura do Repositório](#-estrutura-do-repositório)
3. [🧠 Tópicos de Estudo](#-tópicos-de-estudo)
4. [⚙️ Como Utilizar Este Repositório](#️-como-utilizar-este-repositório)
5. [🚀 Dicas para a Prova](#-dicas-para-a-prova)
6. [📝 Anotações Pessoais](#-anotações-pessoais)

---

## 📖 Introdução

Este repositório é meu **Handbook** 📚 para organizar todos os tópicos e práticas relacionadas à certificação CKAD. O conteúdo aqui será dividido em **kinds** do Kubernetes, dicas para o exame, exemplos práticos, scripts úteis, e anotações que coletei ao longo da jornada.

## 📂 Estrutura do Repositório

```bash
.
├── 📁 01-Pods/
├── 📁 02-Services/
├── 📁 03-ConfigMaps/
├── 📁 04-Secrets/
├── 📁 05-Deployments/
├── 📁 06-RBAC/
├── 📁 07-NetworkPolicies/
└── README.md
```

Cada diretório contém exemplos práticos e anotações sobre o respectivo kind do Kubernetes.

## 🧠 Tópicos de Estudo

Aqui estão os principais tópicos que serão abordados, organizados por **Kind**:

- **Pods** 📦: Configuração, init containers, sidecars
- **Services** 🌐: ClusterIP, NodePort, LoadBalancer
- **ConfigMaps & Secrets** 🗝️: Gestão de configurações sensíveis
- **Deployments** 🚀: Escalabilidade, rollbacks, e mais
- **RBAC** 🔐: Controle de acesso baseado em roles
- **Network Policies** 🔒: Gerenciamento de regras de rede

E mais...

## ⚙️ Como Utilizar Este Repositório

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/ckad-handbook.git
   ```
2. Explore os diferentes **kinds** com exemplos práticos.
3. Use os scripts e templates para testar no seu cluster Kubernetes.

## 🚀 Dicas para a Prova

- Familiarize-se com atalhos de teclado no editor **Vim** ou no **VSCode**.
- Sempre teste as **YAMLs** antes da prova em um ambiente local.
- Utilize ferramentas como o **kubectl cheatsheet** para acelerar sua resolução de problemas.

## 📝 Anotações Pessoais

- ✔️ **Anotação 1**: Lembre-se de sempre verificar os logs do pod quando ocorrerem erros.
- ✔️ **Anotação 2**: Prefira usar `kubectl apply` em vez de `create`, para que as alterações sejam idempotentes.
  
---

Vamos nessa! 💪🎯

---