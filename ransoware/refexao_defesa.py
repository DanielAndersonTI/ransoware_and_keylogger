class ReflexaoDefesa:
    """
    Documentação sobre medidas de prevenção e defesa contra malwares
    """
    
    @staticmethod
    def medidas_prevencao():
        """Lista medidas de prevenção contra ransomware e keyloggers"""
        
        medidas = {
            "Antivírus/Antimalware": [
                "Use soluções reputadas (Bitdefender, Kaspersky, Windows Defender)",
                "Mantenha as definições de vírus atualizadas",
                "Configure varreduras automáticas regulares",
                "Ative proteção em tempo real"
            ],
            
            "Firewall": [
                "Habilite firewall de rede",
                "Configure regras de tráfego de saída",
                "Monitore conexões suspeitas",
                "Use firewall de aplicação"
            ],
            
            "Sandboxing": [
                "Execute arquivos suspeitos em ambiente isolado",
                "Use máquinas virtuais para testes",
                "Implemente contêineres para aplicações",
                "Utilize browsers sandboxed"
            ],
            
            "Conscientização do Usuário": [
                "Não abra anexos de emails desconhecidos",
                "Verifique URLs antes de clicar",
                "Use senhas fortes e autenticação multi-fator",
                "Mantenha sistemas e aplicações atualizados"
            ],
            
            "Backup e Recuperação": [
                "Mantenha backups regulares offline/cloud",
                "Teste restaurações periodicamente",
                "Use a regra 3-2-1 (3 cópias, 2 mídias, 1 offsite)",
                "Proteja backups com senhas fortes"
            ],
            
            "Detecção e Resposta": [
                "Monitore tráfego de rede anômalo",
                "Implemente SIEM/SOC",
                "Configure alertas para atividades suspeitas",
                "Tenha um plano de resposta a incidentes"
            ]
        }
        
        print("🛡️ MEDIDAS DE PREVENÇÃO E DEFESA")
        print("=" * 60)
        
        for categoria, itens in medidas.items():
            print(f"\n📋 {categoria}:")
            for item in itens:
                print(f"   ✅ {item}")
    
    @staticmethod
    def deteccao_ransomware():
        """Sinais de detecção de ransomware"""
        print("\n🔍 SINAIS DE RANSOMWARE:")
        sinais = [
            "Extensões de arquivo alteradas (.encrypted, .locked)",
            "Arquivos de resgate (README.txt, HELP_DECRYPT.html)",
            "Atividade alta de CPU/Disco sem motivo aparente",
            "Acesso a muitos arquivos em sequência",
            "Comunicação com IPs suspeitos"
        ]
        
        for sinal in sinais:
            print(f"   ⚠️ {sinal}")
    
    @staticmethod
    def deteccao_keylogger():
        """Sinais de detecção de keylogger"""
        print("\n🔍 SINAIS DE KEYLOGGER:")
        sinais = [
            "Processos suspeitos no gerenciador de tarefas",
            "Arquivos de log em locais incomuns",
            "Tráfego de rede periódico contendo dados de teclas",
            "Atraso na digitação",
            "Hook de teclado não autorizado"
        ]
        
        for sinal in sinais:
            print(f"   ⚠️ {sinal}")
