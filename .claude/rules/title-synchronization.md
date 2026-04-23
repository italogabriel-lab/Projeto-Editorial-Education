# Sincronização de títulos

## Regra crítica

O arquivo `1 - Curriculo Macro` de cada ano é a única fonte oficial dos títulos.

## Nunca fazer

- Inventar H1 novo.
- Ajustar título por estilo.
- Criar variação poética fora do Currículo Macro.

## Sempre fazer ao detectar divergência

1. Corrigir a partir do Currículo Macro.
2. Executar `trivium-method-editorial/scripts/sync_titles.py`.
3. Confirmar impacto nos arquivos estruturais relacionados.

## Arquivos que precisam permanecer sincronizados

- `1 - Curriculo Macro`
- `2 - Matriz-Curricular-objetivos`
- `3 - Visão e Plano pedagogico`
- `6 - Descrições para tickets`
- Arquivos de aula `.md`
- Revisões semanais `.4.md`

## Sinal de alerta

Se o usuário pedir para renomear aulas, trate o pedido como alteração estrutural e valide tudo contra o Currículo Macro antes de concluir.
