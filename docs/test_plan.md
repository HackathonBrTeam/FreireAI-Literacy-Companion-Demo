# Roteiro de Validacao com Educador

Este roteiro serve para testar a demo FreireIA com um educador de forma simples, sem linguagem tecnica.

O objetivo nao e testar apenas se o botao funciona. O objetivo e descobrir se a solucao ajuda o educador a transformar uma conversa real com o aluno em uma atividade de alfabetizacao critica.

## Antes do teste

Deixe a demo aberta:

```text
http://localhost:8501
```

Use uma configuracao economica no `.env`:

```env
GEMINI_MAX_OUTPUT_TOKENS=250
```

Explique ao educador:

> A FreireIA nao substitui o educador. Ela ajuda a escutar o aluno, organizar o que apareceu na conversa e sugerir uma palavra para criar uma atividade de alfabetizacao.

## Papel de cada pessoa

- Educador: conduz a conversa e decide o que faz sentido pedagogicamente.
- Aluno: fala, aponta, escreve ou escolhe temas/imagens.
- FreireIA: organiza a escuta e sugere caminhos.
- Observador do teste: anota duvidas, travas e comentarios do educador.

## Cenario sugerido para teste

Use este exemplo se nao houver um aluno real no momento:

```text
Aluno adulto, trabalha em mercado, pega onibus cedo, chega cansado e quer aprender a ler mensagens no celular para ajudar a familia.
```

## Passo 1 - Entender a tela inicial

Peca ao educador:

1. Abrir a demo.
2. Olhar as tres abas.
3. Explicar com as proprias palavras o que acha que deve fazer primeiro.

Resultado esperado:

- O educador entende que deve comecar por `1. Escutar`.
- O educador percebe que a ferramenta apoia a conversa, nao substitui sua atuacao.

Perguntas para o educador:

- O primeiro passo ficou claro?
- Alguma palavra da tela parece tecnica demais?
- Voce saberia usar essa tela durante uma conversa real?

## Passo 2 - Preparar perguntas de escuta

Peca ao educador:

1. Ir para `1. Escutar`.
2. Ler o roteiro que ja aparece em `Preparar a conversa`.
3. Dizer se esse roteiro ajudaria a iniciar uma conversa real.

Resultado esperado:

- As perguntas sao simples.
- As perguntas ajudam a iniciar uma conversa com o aluno.
- O educador nao precisa clicar em nada para entender como comecar.

Perguntas para o educador:

- Voce usaria alguma dessas perguntas com um aluno real?
- Alguma pergunta parece artificial ou distante da sala de aula?
- Faltou alguma pergunta importante?

## Passo 3 - Registrar a escuta

Peca ao educador para preencher:

O que o educador percebeu?

```text
Aluno adulto, trabalha em mercado, chega cansado e quer ler melhor mensagens e avisos.
```

O que o aluno falou, escreveu ou apontou?

```text
Eu pego onibus cedo, trabalho o dia todo e quero ler melhor para ajudar em casa.
```

O que chamou atencao?

```text
Pareceu cansado
Pediu ajuda para ler
```

Imagens ou temas escolhidos:

```text
Trabalho
Onibus
Familia
```

Depois, clique em `Sugerir palavras geradoras`.

Resultado esperado:

- A FreireIA resume a escuta.
- A FreireIA sugere palavras como `trabalho`, `onibus`, `familia` ou `casa`.
- Cada palavra vem com uma justificativa simples.
- A FreireIA sugere uma proxima pergunta para o educador.
- A tela mostra uma area clara para escolher a palavra geradora.
- O botao `Usar esta palavra e criar atividade` leva o educador para a proxima etapa.

Perguntas para o educador:

- As palavras sugeridas fazem sentido?
- Qual palavra voce escolheria? Por que?
- A sugestao ajuda ou atrapalha sua decisao pedagogica?
- Ficou claro como escolher a palavra e seguir?

## Passo 4 - Criar atividade

Peca ao educador:

1. Escolher uma palavra na area `Escolher a palavra geradora`.
2. Clicar em `Usar esta palavra e criar atividade`.
3. Confirmar que a tela foi para `2. Criar atividade`.
4. Conferir se a palavra escolhida apareceu preenchida, por exemplo:

```text
trabalho
```

5. Clicar em `Criar atividade de alfabetizacao`.

Resultado esperado:

- A atividade comeca pelo sentido social da palavra.
- A atividade traz perguntas para conversa.
- A atividade inclui leitura, escrita ou separacao silabica/fonetica.
- A linguagem e simples o bastante para uso com o aluno.

Perguntas para o educador:

- Voce aplicaria essa atividade?
- O nivel ficou adequado?
- O que voce mudaria antes de usar com um aluno?

## Passo 5 - Registrar resultado

Peca ao educador:

1. Ir para `3. Registrar resultado`.
2. Marcar o que o aluno conseguiu fazer.
3. Escrever uma frase produzida pelo aluno, por exemplo:

```text
O trabalho ajuda minha familia, mas eu tambem preciso descansar.
```

Resultado esperado:

- O progresso muda conforme os itens sao marcados.
- O registro final ajuda a planejar o proximo encontro.
- O educador entende que nao precisa marcar tudo na primeira sessao.
- A tela permite gerar um relatorio da sessao.
- O relatorio consolida escuta, palavra geradora, atividade e evidencias.
- O relatorio pode ser baixado em Markdown.

Perguntas para o educador:

- Esses criterios fazem sentido para avaliar a sessao?
- Falta algum criterio importante?
- Voce usaria esse registro depois da aula?
- O relatorio seria util para acompanhar o aluno ou conversar com outro educador?

## Passo 6 - Feedback final

Pergunte ao educador:

1. Em que momento a FreireIA mais ajudou?
2. Em que momento ela atrapalhou ou pareceu desnecessaria?
3. A ferramenta respeita o papel do educador?
4. A ferramenta ajuda a escutar melhor o aluno?
5. Que mudanca faria antes de testar com alunos reais?

## Criterios de sucesso da demo

A demo esta boa para apresentar se:

- O educador entende o fluxo sem explicacao longa.
- A interface parece uma sessao pedagogica, nao um painel tecnico.
- A FreireIA sugere palavras conectadas ao contexto do aluno.
- A atividade gerada pode ser usada ou adaptada pelo educador.
- O educador sente que continua no controle da conversa.
- O registro final ajuda a planejar a continuidade da aprendizagem.

## Observacoes para quem conduz o teste

Anote frases exatas do educador, especialmente quando ele disser:

- "Eu usaria isso..."
- "Aqui eu me perdi..."
- "Essa palavra nao faz sentido..."
- "Isso me ajudaria na sala..."

Essas frases sao mais valiosas do que apenas marcar se o teste passou ou falhou.
