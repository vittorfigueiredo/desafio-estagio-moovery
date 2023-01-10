<div align="center">
<img width="160px" heigth="auto" src="https://moovery.com.br/static/media/logoMoovery2.2cf3a421.svg">
</div>

## Descrição:

O desafio consiste no desenvolvimento de um encurtador de url tipo o <strong>bitly.com</strong>.
O desafio está dividido em 3 etapas, portanto, faça o que estiver ao seu alcance e entregue o que conseguiu fazer.

OBS: Use as tecnoligias e ferramentas que preferir.

## FRONTEND:

Crie uma página web para que o usuário insira o link original e realize o encurtamento da url.
Exiba na mesma página ou em outra a parte todos os links convertidos de forma que ao clicar, o usuário seja redirecionado para o link original. Adicione dois botões ao lado dos links que estarão sendo exibidos, um para editar o link e outro para deletar o link.

O que deve ser exibido:

- Id
- Url encurtada
- Data de criação da url encurtada

Obs: Não é obrigatório o uso de <strong>CSS</strong>, mas é interessante que você utilize as folhas de estilo para dar uma aparência mais amigável aos dados apresentados.

## BACKEND:

No backend você deve criar uma API que servirá para realizar as ações vindas do front, são elas:

Busca: Servirá para buscar os dados do banco de dados e retornar para o frontend.

Inserir: Aqui você irá receber do front o link original e salavar no banco da seguinte maneira abaixo:

  Exemplo: http://moove.ry/CvT8P0p7Wd
  
O trecho <strong>http://moove.ry/</strong> não deve ser mudado e todas as urls terão isso em comum. O texto aleatório após a última barra deverá ser gerado automáticamente com um tamanho de <strong>10 caracteres</strong> composto apenas por letras (maiúsculas ou minúsculas) e números.

Atualizar: Servirá para customizar o final de uma url convertida. Aqui o que deve ser atualizado, é somente a parte da url que foi gerada automáticamente.

  Exemplo:

    <strong>Antes:</strong> http://moove.ry/CvT8P0p7Wd
    <strong>Depois de atualizado:</strong> http://moove.ry/<strong>TesteDeExemplo</strong>
    
Deletar: Servirá para excluir o registro do banco de dados.

No backend, você irá precisar realizar uma conexão com um banco de dados. Existem diversas opções, como: MySQL, PostgreSQL, MongoDB, SQLite e etc. Use o que preferir.

O que salvar no banco de dados?

- id
- urlOriginal
- urlCurta
- dataHoraDeCadastro

## DEPLOY: (OPICIONAL)

Está parte não é obrigatória, porém será considerada um diferencial.

Nessa etapa deve ser feita o deploy da aplicação criada por você, ou seja, você irá disponinilizar o projeto na web para quem quiser acessar. Caso consiga fazer essa etapa, insira o link de acesso em um arquivo readmed.md e suba junto com o projeto.

Existem diversas ferramentas pagas e gratuitas para fazer o deploy. Opte, obviamente por uma gratuita.

Exemplos:

https://www.netlify.com/
https://www.heroku.com/

AWS EC2 (Gratuito nos primeiros 12 meses após a criação conta)
Google Cloud (US$ 300 de créditos para gastar nos próximos 90 dias após criação da conta)

Enfim, existem diversas, use a que lhe servir melhor.

Caso precise de um dominio, use o: <strong>freenom.com</strong> para conseguir um grátis por 12 meses. 