# 🛡️ Projeto: Ransomware & Keylogger – Bootcamp Santander Cyber Segurança 2025

Este projeto foi desenvolvido como parte do Bootcamp Santander Cyber Segurança 2025, com o objetivo de aplicar conceitos de segurança ofensiva em ambientes controlados. As ferramentas criadas simulam comportamentos reais de ameaças cibernéticas, permitindo o estudo aprofundado de técnicas utilizadas em pentests e análise forense.

---

## 📌 Objetivos

- Desenvolver um **ransomware funcional** com criptografia e mensagem de resgate.
- Criar um **keylogger furtivo** com envio automático de logs via e-mail.
- Compreender o ciclo de ataque, evasão e exfiltração de dados.
- Aplicar boas práticas de desenvolvimento seguro e ético.

---

## 🧰 Tecnologias Utilizadas

| Tecnologia       | Finalidade                                                                 |
|------------------|------------------------------------------------------------------------------|
| **Python**       | Linguagem principal para desenvolvimento dos scripts                        |
| **pynput**       | Captura de eventos do teclado para o keylogger                              |
| **smtplib**      | Envio de e-mails via protocolo SMTP                                         |
| **email.mime**   | Formatação de mensagens para envio de logs                                  |
| **threading.Timer** | Execução periódica do envio de dados capturados                         |
| **cryptography** | Criptografia simétrica de arquivos no ransomware                            |
| **pip**          | Gerenciador de pacotes para instalação das bibliotecas                      |
| **stdlib**       | Utilitários nativos do Python para manipulação de arquivos e sistema        |

---

## 🔐 Módulo 1 – Ransomware

- Criptografa arquivos específicos ou diretórios inteiros.
- Utiliza chave secreta para descriptografia.
- Exibe mensagem de resgate simulando ataque real.
- Permite segmentação por extensão de arquivo.

---

## 🎹 Módulo 2 – Keylogger

- Captura de teclas com filtragem de caracteres indesejáveis.
- Execução furtiva com extensão `.pyw` para ocultar janela no Windows.
- Envio automático dos logs via e-mail a cada 60 segundos.
- Autenticação em duas etapas com senha de aplicativo no Gmail.

---

## ⚠️ Aviso Legal

Este projeto foi desenvolvido **exclusivamente para fins educacionais** em ambiente controlado. O uso indevido das ferramentas aqui descritas pode violar leis de privacidade e segurança digital. Sempre obtenha autorização explícita antes de realizar qualquer teste de intrusão.

---

## 📞 Contato

**Autor:** Daniel  
**Local:** João Pessoa, PB  
**LinkedIn:** (https://www.linkedin.com/in/daniel-anderson-275379296/)  
**GitHub:** (https://github.com/DanielAndersonTI?tab=repositories)
---


## 📂 Estrutura do Projeto

