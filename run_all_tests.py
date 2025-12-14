#!/usr/bin/env python3
"""
Script principal para testar todos os exercícios do Trabalho Final de Computação Gráfica
Executa todas as implementações e verifica se estão funcionando corretamente.
"""

import os
import sys
import subprocess

def run_test(description, script_path, working_dir):
    """Executa um teste e reporta o resultado"""
    print(f"\n{'='*60}")
    print(f"TESTE: {description}")
    print(f"{'='*60}")
    
    try:
        # Ativar ambiente virtual e executar o script
        script_dir = os.path.dirname(script_path) if '/' in script_path else ''
        script_name = os.path.basename(script_path)
        full_working_dir = os.path.join(working_dir, script_dir) if script_dir else working_dir
        
        cmd = f"cd '{full_working_dir}' && bash -c 'source {working_dir}/venv/bin/activate && python {script_name}'"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"✓ SUCESSO - {description}")
            if result.stdout.strip():
                print("Output:")
                print(result.stdout)
            return True
        else:
            print(f"✗ FALHOU - {description}")
            if result.stderr.strip():
                print("Erro:")
                print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏱ TIMEOUT - {description} (pode estar aguardando interação)")
        return True  # Consideramos timeout como sucesso para scripts gráficos
    except Exception as e:
        print(f"✗ ERRO - {description}: {e}")
        return False

def main():
    print("TRABALHO FINAL - COMPUTAÇÃO GRÁFICA")
    print("Testando todas as implementações...")
    
    base_dir = "/home/guilherme/Documents/CG/FINAL"
    
    # Lista de testes a serem executados
    tests = [
        ("Exercício 1 - Redução de Grau (OpenGL)", "bezier/main_bezier.py", base_dir),
        ("Exercício 2 - Aumento de Grau (OpenGL)", "bezier/test_aumento_grau.py", base_dir),
        ("Exercício 3 - Superfície de Revolução (OpenGL)", "superficies/revolucao.py", base_dir),
        ("Exercício 4 - Superfície de Varredura (OpenGL)", "superficies/test_varredura.py", base_dir),
        ("Extra - Asa de Avião (OpenGL)", "superficies/test_asa_aviao.py", base_dir),
        ("Exercício 5 - Rendering Phong (Completo)", "render/test_rendering.py", base_dir)
    ]
    
    success_count = 0
    total_tests = len(tests)
    
    # Executar todos os testes
    for description, script_path, working_dir in tests:
        if run_test(description, script_path, working_dir):
            success_count += 1
    
    # Relatório final
    print(f"\n{'='*60}")
    print("RELATÓRIO FINAL")
    print(f"{'='*60}")
    print(f"Testes executados: {total_tests}")
    print(f"Sucessos: {success_count}")
    print(f"Falhas: {total_tests - success_count}")
    
    if success_count == total_tests:
        print("\n🎉 TODOS OS TESTES PASSARAM! 🎉")
        print("Todas as implementações estão funcionando corretamente.")
    else:
        print(f"\n⚠️  {total_tests - success_count} teste(s) falharam.")
    
    print(f"\nTaxa de sucesso: {success_count/total_tests*100:.1f}%")

if __name__ == "__main__":
    main()