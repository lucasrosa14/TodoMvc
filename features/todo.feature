Feature: Gerenciar tarefas no TodoMVC

  Scenario: Adicionar uma tarefa à lista
    Given que eu estou na página inicial
    When eu adiciono uma nova tarefa com o nome "Estudar BDD"
    Then a tarefa "Estudar BDD" deve ser exibida na lista de tarefas

  Scenario: Adicionar várias tarefas
    Given que eu estou na página inicial
    When eu adiciono uma nova tarefa com o nome "Tarefa 1"
    When eu adiciono uma nova tarefa com o nome "Tarefa 2"
    Then a tarefa "Tarefa 1" deve ser exibida na lista de tarefas
    Then a tarefa "Tarefa 2" deve ser exibida na lista de tarefas

  Scenario: Concluir uma tarefa
    Given que eu estou na página inicial
    When eu adiciono uma nova tarefa com o nome "Tarefa para concluir"
    When eu clico na tarefa "Tarefa para concluir"
    Then a tarefa "Tarefa para concluir" deve ser exibida na lista de tarefas
    Then a tarefa "Tarefa para concluir" deve ser marcada como concluída

  Scenario: Filtrar tarefas ativas
    Given que eu estou na página inicial
    When eu adiciono uma nova tarefa com o nome "Tarefa ativa"
    Then a tarefa "Tarefa ativa" deve ser exibida na lista de tarefas
    When eu clico na tarefa "Tarefa ativa"
    Then a tarefa "Tarefa ativa" deve ser marcada como concluída
    When eu filtro as tarefas ativas
    Then a lista de tarefas deve exibir apenas tarefas ativas

  Scenario: Filtrar tarefas concluídas
    Given que eu estou na página inicial
    When eu adiciono uma nova tarefa com o nome "Tarefa concluída"
    Then a tarefa "Tarefa concluída" deve ser exibida na lista de tarefas
    When eu clico na tarefa "Tarefa concluída"
    Then a tarefa "Tarefa concluída" deve ser marcada como concluída
    When eu filtro as tarefas concluídas
    Then a lista de tarefas deve exibir apenas tarefas concluídas
