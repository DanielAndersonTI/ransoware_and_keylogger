# 🛡️ Relatório Técnico – Bootcamp Santander Cyber Segurança 2025

**Participante:** Daniel  
**Data de conclusão:** Outubro de 2025  
**Local:** João Pessoa, PB  
**Tecnologias utilizadas:** Python, Pynput, SMTP, pip, stdlib, criptografia simétrica

---

## 🎯 Objetivo da Atividade

A atividade teve como foco o desenvolvimento prático de duas ferramentas comumente utilizadas em testes de intrusão (pentests): um **ransomware** e um **keylogger**. O objetivo foi compreender o funcionamento interno dessas ferramentas, reforçar conceitos de segurança ofensiva e preparar os participantes para desenvolver soluções de análise e defesa em ambientes reais.

---

## 🔐 Módulo 1 – Ransomware

Foi desenvolvido um script de ransomware com as seguintes funcionalidades:

- **Criptografia de arquivos**: Utilização de biblioteca de criptografia simétrica (ex.: `cryptography.fernet`) para codificar arquivos específicos ou diretórios inteiros.
- **Descriptografia controlada**: Mecanismo de reversão mediante chave secreta.
- **Mensagem de resgate**: Exibição de mensagem simulando um pedido de resgate, como ocorre em ataques reais.
- **Segmentação de arquivos**: Seleção de extensões específicas (.txt, .docx, .pdf etc.) para ataque direcionado.

Essa abordagem permitiu entender como atacantes estruturam ameaças e como ferramentas de defesa podem ser projetadas para mitigar esse tipo de risco.

---

## 🎹 Módulo 2 – Keylogger

O segundo módulo envolveu a criação de um keylogger funcional com envio de dados via e-mail. As etapas foram:

- **Captura de teclas**: Monitoramento e registro de entradas do teclado com a biblioteca `pynput`.
- **Filtragem de caracteres**: Implementação de exceções para ignorar teclas irrelevantes ou de controle, facilitando a leitura dos logs.
- **Execução furtiva**:
  - Versão `.py`: visível, útil para testes e depuração.
  - Versão `.pyw`: oculta, ideal para execução silenciosa no Windows.
- **Envio automático via SMTP**:
  - Configuração de conta Gmail dedicada com autenticação em duas etapas.
  - Geração de senha de aplicativo para envio automatizado dos logs.
  - Envio periódico dos dados capturados (ex.: a cada 60 segundos), simulando exfiltração real.

---

## 🧰 Tecnologias e Ferramentas

| Tecnologia       | Aplicação                                      |
|------------------|------------------------------------------------|
| Python           | Linguagem principal do projeto                 |
| Pynput           | Captura de eventos do teclado                  |
| SMTP (smtplib)   | Envio de e-mails com os logs do keylogger      |
| MIMEText         | Formatação de mensagens para envio             |
| Cryptography     | Criptografia simétrica de arquivos (ransomware)|
| pip              | Gerenciador de pacotes                         |
| stdlib           | Utilitários nativos do Python                  |

---

## 📌 Considerações Finais

A atividade proporcionou uma compreensão prática e ética sobre ferramentas utilizadas em segurança ofensiva. Ao simular comportamentos maliciosos em ambiente controlado, foi possível:

- Identificar vulnerabilidades comuns.
- Compreender técnicas de evasão e persistência.
- Aprimorar habilidades em automação e análise de comportamento.

Esses conhecimentos são fundamentais para profissionais que atuam com **pentest, análise forense, resposta a incidentes** e **desenvolvimento de soluções de segurança**.
