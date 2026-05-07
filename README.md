# Práctica: Control de Versiones con Git y GitHub

**Curso:** Ingeniería en Sistemas
**Modalidad:** Práctica de laboratorio

---

## Objetivos de aprendizaje

Al finalizar la práctica, usted deberá ser capaz de:

1. Explicar qué es un sistema de control de versiones distribuido y por qué Git es el estándar de la industria.
2. Aplicar el flujo de trabajo básico de Git (`add`, `commit`, `status`, `log`) sobre un proyecto real.
3. Gestionar ramas: crearlas, fusionarlas y eliminarlas siguiendo buenas prácticas.
4. Distinguir cuándo usar `git reset` y cuándo usar `git revert`, justificando la decisión.
5. Etiquetar versiones del software con `git tag` y navegar el historial con `git checkout`.
6. Resolver conflictos de fusión de manera consciente, entendiendo qué se está conservando y qué se está descartando.
7. Operar Git desde la integración de Visual Studio Code, identificando equivalencias con la línea de comandos.
8. Trabajar con repositorios remotos en GitHub: crear, clonar, sincronizar (`pull`, `push`, `fetch`) y colaborar mediante Pull Requests.
9. Construir una portada de perfil profesional en GitHub usando Markdown.

---

## Requisitos previos

Antes de comenzar, asegúrese de contar con:

- Git instalado (`git --version` debe responder con una versión 2.30 o superior).
- Una cuenta personal en [github.com](https://github.com).
- Visual Studio Code instalado.
- Un editor de texto plano disponible (el mismo VS Code sirve).
- Configuración inicial de Git realizada:

```bash
git config --global user.name "Su Nombre Apellido"
git config --global user.email "[email protected]"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
```

> **Por qué importa esta configuración:** Cada commit lleva una firma con su nombre y correo. Si trabaja en una organización, esa firma se vincula con su identidad de GitHub y aparece en el historial público. Configurarlo mal desde el inicio le va a costar reescribir historial más adelante.

---


### ¿Qué es Git?

Git es un **sistema de control de versiones distribuido (DVCS)**. "Distribuido" significa que cada copia del repositorio es completa: no depende de un servidor central para funcionar. Usted puede trabajar sin internet, hacer commits, crear ramas y luego sincronizar.

### Las tres áreas de Git

Cuando edita un archivo en un proyecto Git, ese archivo puede estar en una de estas tres áreas:

1. **Working Directory (directorio de trabajo):** los archivos como los ve en su explorador. Aquí edita.
2. **Staging Area (área de preparación o índice):** una "antesala" donde marca qué cambios quiere incluir en el próximo commit. Es lo que diferencia a Git de otros sistemas: le da control fino sobre qué va a guardar.
3. **Repository (repositorio):** la base de datos histórica de commits. Una vez que algo está acá, queda registrado.

El flujo es: **edita → `git add` (lo manda al staging) → `git commit` (lo guarda en el repositorio)**.

### ¿Qué es un commit?

Un commit es una **fotografía inmutable del proyecto** en un momento dado. Tiene:

- Un identificador único (hash SHA-1, ejemplo: `a1b2c3d...`).
- Un autor y una fecha.
- Un mensaje descriptivo.
- Un puntero al commit padre (o a varios padres si es un merge).

> **Idea clave:** Git no guarda "diferencias" entre versiones, guarda **fotos completas** y luego optimiza espacio internamente. Por eso puede moverse entre commits casi instantáneamente.

### ¿Qué es una rama?

Una rama es un **puntero móvil a un commit**. Nada más. Cuando hace un nuevo commit en una rama, el puntero avanza. Por eso ramificar en Git es barato (no copia archivos, solo crea un puntero nuevo).

### ¿Qué es HEAD?

`HEAD` es un puntero especial que indica **dónde está usted parado** en el historial. Normalmente apunta a la rama activa.

---

## Parte 1: Git local

### Sección 1: Comandos básicos y flujo de trabajo

#### Conceptos

El ciclo más común de trabajo es:

```
[edita archivos]  →  git status  →  git add  →  git commit  →  git log
```

| Comando | Para qué sirve |
|---------|----------------|
| `git init` | Convierte una carpeta en un repositorio Git |
| `git status` | Muestra qué archivos cambiaron y en qué área están |
| `git add <archivo>` | Marca un archivo para incluirlo en el próximo commit |
| `git add .` | Marca todos los cambios del directorio actual |
| `git commit -m "mensaje"` | Guarda los cambios marcados con un mensaje |
| `git log` | Muestra el historial de commits |
| `git log --oneline --graph --all` | Vista compacta y gráfica de toda la historia |
| `git diff` | Muestra qué cambió en archivos no añadidos |
| `git diff --staged` | Muestra qué cambió en archivos ya añadidos |

#### Buenas prácticas para mensajes de commit

- Use el imperativo: `"Agrega validación de email"` (no `"Agregué"` ni `"Agregando"`).
- La primera línea no debe pasar de 50 caracteres.
- Si hace falta más detalle, deje una línea en blanco y luego un párrafo explicando el **por qué**.
- Un commit debe representar **una idea coherente**, no "guardé todo lo del día".

#### Ejercicio 1.1: Inicializar y primer commit

**Enunciado:**

1. Cree una carpeta llamada `practica-git` en su escritorio.
2. Inicialícela como repositorio Git.
3. Cree un archivo `README.md` con el texto: `# Práctica de Git`.
4. Verifique el estado del repositorio.
5. Añada el archivo al staging y haga el primer commit con un mensaje descriptivo.
6. Muestre el log del repositorio.

**Pista:** Use `git status` después de cada paso para ir entendiendo qué hace Git internamente.

**Solución:**

```bash
# 1 y 2
mkdir practica-git
cd practica-git
git init

# 3
echo "# Práctica de Git" > README.md

# 4
git status
# Salida esperada: README.md aparece en "Untracked files"

# 5
git add README.md
git status
# Salida esperada: README.md aparece en "Changes to be committed"

git commit -m "Crea archivo README inicial del proyecto"

# 6
git log
```

**Explicación:** En el paso 4, el archivo está en el working directory pero Git aún no lo "conoce". Cuando hace `git add`, lo mueve al staging. Cuando hace `commit`, lo registra en el repositorio. Este flujo de tres etapas es lo que le da a Git el control fino sobre qué incluir en cada versión.

#### Ejercicio 1.2: Múltiples archivos y commits selectivos

**Enunciado:**

1. En la misma carpeta, cree tres archivos: `index.html`, `estilos.css`, `notas.txt`.
2. Edite cada uno con contenido cualquiera.
3. Haga **dos commits separados**: uno que incluya solamente `index.html` y `estilos.css`, y otro que incluya `notas.txt`.

**Solución:**

```bash
# 1 y 2 - cree los archivos con cualquier contenido
echo "<html><body><h1>Hola</h1></body></html>" > index.html
echo "body { font-family: sans-serif; }" > estilos.css
echo "Recordar revisar la práctica" > notas.txt

# 3 - primer commit selectivo
git add index.html estilos.css
git commit -m "Agrega estructura base HTML y estilos"

# Segundo commit
git add notas.txt
git commit -m "Agrega archivo de notas personales"

git log --oneline
```

**Explicación:** Este ejercicio demuestra el valor del staging area. En otros sistemas (como SVN clásico), un commit guarda **todo** lo modificado. Git le permite separar cambios lógicamente diferentes en commits distintos, aunque los haya hecho en la misma sesión.

---

### Sección 2: Gestión de ramas

#### Conceptos

Trabajar siempre en `main` es como editar un documento sin tener copia de respaldo: cualquier experimento puede romper lo que ya funciona. Las ramas resuelven esto.

**Cuándo crear una rama:**

- Para una nueva funcionalidad (`feature/login`)
- Para corregir un error (`fix/validacion-correo`)
- Para experimentar (`exp/nuevo-diseno`)

**Convención de nombres recomendada:**

```
feature/<descripcion-corta>
fix/<descripcion-corta>
hotfix/<descripcion-corta>
release/<version>
```

#### Comandos esenciales

| Comando | Para qué sirve |
|---------|----------------|
| `git branch` | Lista las ramas locales |
| `git branch <nombre>` | Crea una rama (no la cambia) |
| `git checkout <nombre>` | Cambia a una rama existente |
| `git checkout -b <nombre>` | Crea y cambia a la rama (atajo común) |
| `git switch <nombre>` | Cambia de rama (alternativa moderna a checkout) |
| `git switch -c <nombre>` | Crea y cambia (equivale a `checkout -b`) |
| `git merge <rama>` | Fusiona una rama con la actual |
| `git branch -d <nombre>` | Elimina una rama (solo si fue fusionada) |
| `git branch -D <nombre>` | Elimina forzando (descarta cambios no fusionados) |

> **Nota técnica:** `git switch` y `git restore` se introdujeron en Git 2.23 para separar responsabilidades que `checkout` mezclaba (cambiar ramas vs. restaurar archivos). En la industria todavía se ve mucho `checkout`, pero acostúmbrese a `switch` cuando se trate solo de cambiar de rama.

#### Tipos de fusión

1. **Fast-forward:** cuando la rama destino no avanzó desde que se creó la rama hija. Git solo "mueve el puntero". No se crea un commit de merge.
2. **Three-way merge:** cuando ambas ramas avanzaron. Git crea un **commit de merge** con dos padres.

Forzar siempre un commit de merge (aunque sea fast-forward) ayuda a leer la historia: se ve claramente "acá entró tal feature".

```bash
git merge --no-ff feature/login   # crea commit de merge incluso si fuera fast-forward
```

#### Ejercicio 2.1: Crear, fusionar y eliminar una rama

**Enunciado:**

1. Estando en `main`, cree una rama llamada `feature/saludo`.
2. Cámbiese a esa rama.
3. Cree un archivo `saludo.txt` con el texto `"Hola mundo"` y haga commit.
4. Vuelva a `main` y verifique que el archivo no está.
5. Fusione la rama `feature/saludo` en `main`.
6. Verifique que ahora sí aparece el archivo.
7. Elimine la rama `feature/saludo`.

**Solución:**

```bash
# 1 y 2 (en una sola línea con -b)
git checkout -b feature/saludo

# 3
echo "Hola mundo" > saludo.txt
git add saludo.txt
git commit -m "Agrega archivo de saludo"

# 4
git checkout main
ls
# saludo.txt NO aparece, porque está solo en la otra rama

# 5
git merge feature/saludo
# Salida: Fast-forward (porque main no avanzó)

# 6
ls
# Ahora sí aparece saludo.txt

# 7
git branch -d feature/saludo
```

**Explicación:** En el paso 4 está la idea más importante: las ramas son **realidades paralelas** del proyecto. Git cambia físicamente los archivos en su disco al cambiar de rama. En el paso 5 se vio un fast-forward porque `main` no había avanzado.

#### Ejercicio 2.2: Merge con divergencia (three-way)

**Enunciado:**

1. Desde `main`, cree la rama `feature/info`.
2. En `feature/info`, agregue una línea `Información del proyecto` al final de `README.md` y haga commit.
3. Vuelva a `main` y agregue una línea distinta (`Proyecto creado por X`) al final de `README.md`. Haga commit.
4. Fusione `feature/info` en `main`.
5. Observe el resultado y resuelva el conflicto si aparece.

**Solución parcial (la resolución de conflictos se trabaja en la Sección 5):**

```bash
git checkout -b feature/info
echo "Información del proyecto" >> README.md
git add README.md
git commit -m "Agrega sección de información"

git checkout main
echo "Proyecto creado por X" >> README.md
git add README.md
git commit -m "Agrega autoría del proyecto"

git merge feature/info
# Va a aparecer un conflicto, lo resolvemos en la Sección 5
```

---

### Sección 3: `git reset` vs `git revert`

#### El problema

Cometió un error y necesita "deshacer" un commit. Git ofrece dos caminos con filosofías opuestas:

- **`git reset`:** **reescribe la historia.** Mueve el puntero de la rama hacia atrás y, opcionalmente, elimina los commits del historial.
- **`git revert`:** **agrega historia.** Crea un nuevo commit que **deshace** los cambios del commit señalado, dejando el historial original intacto.

#### Regla de oro

> **`reset` se usa en commits que NO ha compartido (no han sido pusheados). `revert` se usa en commits que YA compartió con el equipo.**

¿Por qué? Porque `reset` reescribe historia. Si su compañero ya bajó esos commits, reescribirlos en el remoto va a generar un caos: divergencias que ni Git puede arreglar limpiamente.

#### Variantes de `git reset`

```bash
git reset --soft <commit>    # mueve HEAD; deja cambios en staging
git reset --mixed <commit>   # mueve HEAD; deja cambios en working dir (DEFAULT)
git reset --hard <commit>    # mueve HEAD; DESCARTA cambios (peligroso)
```

| Modo | Working Directory | Staging | Repositorio |
|------|------|---------|-------------|
| `--soft` | Conserva | Conserva | Mueve HEAD |
| `--mixed` | Conserva | Limpia | Mueve HEAD |
| `--hard` | Limpia | Limpia | Mueve HEAD |

> **`--hard` borra trabajo.** Si lo ejecuta sin haber hecho commit de cambios importantes, esos cambios desaparecen. Use con precaución.

#### Ejercicio 3.1: `reset --soft`

**Enunciado:**

1. En `main`, cree un archivo `temporal.txt` con cualquier contenido y haga commit.
2. Verifique que el commit aparece en `git log`.
3. Use `git reset --soft HEAD~1` para deshacer el commit, conservando los cambios en staging.
4. Observe el estado con `git status`.
5. Decida: o bien hace nuevamente commit con un mejor mensaje, o desecha los cambios con `git restore --staged temporal.txt && rm temporal.txt`.

**Solución:**

```bash
# 1
echo "contenido temporal" > temporal.txt
git add temporal.txt
git commit -m "agregue cosa"   # mensaje pobre a propósito

# 2
git log --oneline

# 3
git reset --soft HEAD~1
# HEAD~1 significa "el commit anterior a HEAD"

# 4
git status
# El archivo está en staging, listo para un nuevo commit

# 5 - opción A: re-commit con mensaje mejor
git commit -m "Agrega archivo temporal de prueba para flujo de Git"
```

**Explicación:** `HEAD~1` es notación relativa: "un commit antes del actual". `HEAD~2` sería dos antes, etc. Esta técnica es muy común para corregir el último mensaje de commit (aunque también se puede usar `git commit --amend`).

#### Ejercicio 3.2: `git revert`

**Enunciado:**

1. En `main`, haga un commit que agregue un archivo `error.txt`.
2. Haga después dos o tres commits más con cambios menores en `README.md`.
3. Suponga que `error.txt` no debería existir, pero los commits posteriores sí deben permanecer.
4. Use `git revert` sobre el commit del paso 1 sin afectar los commits posteriores.

**Solución:**

```bash
# 1
echo "esto no debería estar" > error.txt
git add error.txt
git commit -m "Agrega archivo error"

# 2
echo "linea A" >> README.md && git commit -am "Mejora 1 README"
echo "linea B" >> README.md && git commit -am "Mejora 2 README"

# 3 y 4
git log --oneline
# Identificamos el hash del commit a revertir, ejemplo: a1b2c3d
git revert a1b2c3d
# Git abre el editor para confirmar el mensaje del nuevo commit
# Se crea un commit que ELIMINA error.txt, sin tocar los demás
```

**Explicación:** Con `revert`, los commits intermedios quedan exactamente como estaban. Lo único que cambia es que se agrega un commit nuevo al final, que invierte los cambios del commit objetivo. Esto es lo correcto cuando ya empujó al remoto: la historia compartida no se altera, solo se le suma información.

---

### Sección 4: `git tag` y `git checkout` para gestión de versiones

#### Conceptos

Un **tag** es una etiqueta sobre un commit específico. A diferencia de las ramas, los tags **no se mueven**: marcan un punto fijo en la historia. Se usan principalmente para marcar **versiones liberadas** (`v1.0.0`, `v2.1.3`).

#### Tipos de tags

1. **Lightweight (ligero):** un puntero simple a un commit. Solo nombre.
2. **Annotated (anotado):** lleva metadata (autor, fecha, mensaje, firma opcional). **Es el recomendado para releases.**

```bash
# Lightweight
git tag v1.0

# Annotated (recomendado)
git tag -a v1.0 -m "Versión 1.0 - primera release pública"
```

#### Comandos útiles

| Comando | Para qué sirve |
|---------|----------------|
| `git tag` | Lista todos los tags |
| `git tag -a v1.0 -m "..."` | Crea tag anotado en el commit actual |
| `git tag -a v1.0 <hash>` | Crea tag anotado en un commit específico |
| `git show v1.0` | Muestra detalles del tag |
| `git tag -d v1.0` | Elimina un tag local |
| `git push origin v1.0` | Sube un tag al remoto |
| `git push origin --tags` | Sube todos los tags al remoto |

#### `git checkout` para navegación

Aparte de cambiar de rama, `git checkout <hash>` le permite "viajar en el tiempo" al estado de un commit específico. Esto lo deja en estado **detached HEAD** (HEAD desconectado).

> **¿Qué es detached HEAD?** Significa que HEAD ya no apunta a ninguna rama, sino directamente a un commit. Si hace cambios y commits acá, esos commits no pertenecen a ninguna rama: se "pierden" al cambiar de rama. Para conservarlos, debe crear una rama desde ese punto: `git switch -c rescate`.

#### Ejercicio 4.1: Etiquetar una versión

**Enunciado:**

1. En `main`, asegúrese de tener al menos tres commits.
2. Cree un tag anotado `v1.0` en el último commit con el mensaje `"Versión inicial estable"`.
3. Haga otro commit (cualquier cambio menor).
4. Cree un tag anotado `v1.1` en el commit nuevo.
5. Liste los tags y muestre los detalles de `v1.0`.

**Solución:**

```bash
# 1 - asumimos que ya hay commits
git log --oneline

# 2
git tag -a v1.0 -m "Versión inicial estable"

# 3
echo "ajuste menor" >> README.md
git commit -am "Ajuste menor de documentación"

# 4
git tag -a v1.1 -m "Versión 1.1 con ajustes de documentación"

# 5
git tag
git show v1.0
```

#### Ejercicio 4.2: Viajar a una versión anterior

**Enunciado:**

1. Desde `main`, use `git checkout v1.0` para volver a la versión etiquetada como `v1.0`.
2. Inspeccione los archivos: deberían ser los del momento en que se creó el tag.
3. Lea el mensaje que Git le muestra sobre detached HEAD.
4. Vuelva a `main` con `git switch main`.

**Solución:**

```bash
git checkout v1.0
ls
cat README.md
# Está viendo el estado del proyecto en v1.0

# Mensaje típico de Git:
# "You are in 'detached HEAD' state..."
# Esto NO es un error. Git le avisa que está fuera de cualquier rama.

git switch main
```

**Explicación:** El detached HEAD es útil para inspeccionar versiones antiguas, hacer pruebas puntuales, o aplicar un parche en una versión anterior. Si decide trabajar desde ese punto, cree una rama: `git switch -c hotfix/v1.0-parche`.

---

### Sección 5: Resolución de conflictos

#### ¿Cuándo aparece un conflicto?

Cuando dos ramas modifican **la misma porción del mismo archivo** y Git no puede decidir automáticamente cuál cambio prevalece. Git no rompe el archivo: lo deja con marcadores especiales para que **usted** decida.

#### Anatomía de un conflicto

Después de un merge con conflicto, abra el archivo afectado y verá:

```
<<<<<<< HEAD
Línea según la rama actual (main)
=======
Línea según la rama que está fusionando (feature/info)
>>>>>>> feature/info
```

Su trabajo es:

1. Decidir qué versión conservar (o combinar ambas).
2. Eliminar los marcadores `<<<<<<<`, `=======`, `>>>>>>>`.
3. Guardar el archivo.
4. `git add` del archivo resuelto.
5. `git commit` para finalizar el merge.

#### Comandos útiles

```bash
git status                  # muestra archivos en conflicto
git diff                    # muestra los conflictos
git merge --abort           # cancela el merge y vuelve al estado anterior
git mergetool               # abre una herramienta visual configurada
```

#### Ejercicio 5.1: Provocar y resolver un conflicto

**Enunciado:**

1. En `main`, asegúrese de que `README.md` tenga este contenido:

   ```
   # Práctica de Git
   Autor: Pendiente
   ```

2. Cree la rama `feature/autor-rony` y cambie la línea `Autor: Pendiente` por `Autor: Rony`. Haga commit.
3. Vuelva a `main` y, sin fusionar, cambie la misma línea por `Autor: Equipo de Desarrollo`. Haga commit.
4. Intente fusionar `feature/autor-rony` en `main`.
5. Resuelva el conflicto conservando: `Autor: Rony y Equipo de Desarrollo`.
6. Complete el merge.

**Solución:**

```bash
# 1 - aseguramos contenido de partida
cat > README.md << 'EOF'
# Práctica de Git
Autor: Pendiente
EOF
git add README.md
git commit -m "Estado base del README para conflicto"

# 2
git checkout -b feature/autor-rony
# Edite README.md y deje:
# # Práctica de Git
# Autor: Rony
git add README.md
git commit -m "Asigna autor: Rony"

# 3
git checkout main
# Edite README.md y deje:
# # Práctica de Git
# Autor: Equipo de Desarrollo
git add README.md
git commit -m "Asigna autor: Equipo"

# 4
git merge feature/autor-rony
# Salida: CONFLICT (content): Merge conflict in README.md

# 5 - abra README.md y verá:
# <<<<<<< HEAD
# Autor: Equipo de Desarrollo
# =======
# Autor: Rony
# >>>>>>> feature/autor-rony
#
# Edítelo manualmente para que quede:
# # Práctica de Git
# Autor: Rony y Equipo de Desarrollo

# 6
git add README.md
git commit -m "Resuelve conflicto de autoría combinando ambas versiones"

git log --oneline --graph --all
```

**Explicación:** El conflicto **no es un error de Git**, es Git pidiéndole una decisión humana. La pregunta que debe hacerse al resolver no es "¿cuál marcador borro?" sino "¿qué tiene sentido en el negocio?". A veces la respuesta es "ninguna de las dos, escribo algo nuevo".

---

### Sección 6: Git en Visual Studio Code

#### Conceptos

VS Code integra Git a través de la pestaña **Source Control** (icono con tres nodos conectados, atajo `Ctrl+Shift+G`). Internamente ejecuta los mismos comandos que usted aprendió en CLI.

> **Por qué importa la equivalencia:** los IDEs son cómodos, pero un día algo va a fallar y necesitará entender qué está pasando "debajo". Si solo conoce los botones, está atrapado.

#### Equivalencia botón → comando

| Acción en VS Code | Comando equivalente |
|--|--|
| Símbolo `+` junto al archivo | `git add <archivo>` |
| Botón "Commit" con mensaje | `git commit -m "..."` |
| `...` → "Push" | `git push` |
| `...` → "Pull" | `git pull` |
| `...` → "Branch → Create Branch" | `git checkout -b <nombre>` |
| Icono de rama abajo a la izquierda | `git branch` (selector visual) |
| Vista de cambios (diff lateral) | `git diff` |
| Resolución gráfica de conflictos | Edición manual + `git add` |

#### Extensiones recomendadas

- **GitLens:** muestra autoría línea por línea, historial, comparaciones avanzadas.
- **Git Graph:** representación visual del árbol de commits y ramas.
- **Git History:** historial detallado por archivo.

#### Ejercicio 6.1: Workflow completo desde VS Code

**Enunciado:**

1. Abra el proyecto `practica-git` en VS Code.
2. Cree una rama nueva llamada `feature/vscode-test` desde el selector inferior izquierdo.
3. Cree un archivo `vscode.txt` con cualquier contenido.
4. Desde la pestaña Source Control, agregue el archivo al staging (símbolo `+`).
5. Escriba un mensaje de commit y presione el botón de Commit.
6. Cambie a `main` desde el selector.
7. Fusione `feature/vscode-test` desde el menú `...` → `Branch → Merge Branch`.
8. Verifique en una terminal que el resultado coincide con lo que vería desde CLI.

**Solución (verificación CLI tras cada paso):**

```bash
# Tras paso 2:
git branch
# * feature/vscode-test

# Tras paso 5:
git log --oneline -1
# Verá su commit hecho desde VS Code

# Tras paso 7:
git log --oneline --graph --all
```

**Reflexión:** Note que VS Code no inventa nada nuevo. Cada acción gráfica deja un rastro idéntico al que dejaría desde la terminal. Esto le da libertad: puede combinar ambos enfoques según convenga.

---

## Parte 2: GitHub

### Sección 7: Repositorios remotos

#### Conceptos

**Git** es la herramienta de control de versiones. **GitHub** es un servicio web que **hospeda repositorios Git** y agrega capas de colaboración (Pull Requests, Issues, Actions, Projects).

Otras alternativas similares: GitLab, Bitbucket, Gitea, Codeberg.

#### Modelo mental

```
[su laptop: repositorio local]  ⇄  [github.com: repositorio remoto]
                              git push / pull / fetch
```

El repositorio remoto típicamente se llama **`origin`**. Es solo una etiqueta convencional, no una palabra mágica.

#### Crear un repositorio en GitHub

1. Inicie sesión en [github.com](https://github.com).
2. Click en **"+"** (esquina superior derecha) → **New repository**.
3. Complete:
   - **Repository name:** `practica-git`
   - **Description:** breve descripción.
   - **Visibility:** Public o Private.
   - **NO** marque "Add a README" si ya tiene uno local (evita conflictos al primer push).
4. Click en **Create repository**.

#### Vincular repo local con remoto

GitHub le mostrará dos casos: "create new" y "push existing". Para nuestra práctica, el segundo:

```bash
git remote add origin https://github.com/su-usuario/practica-git.git
git branch -M main
git push -u origin main
```

| Comando | Para qué sirve |
|---------|----------------|
| `git remote add <nombre> <url>` | Vincula un remoto |
| `git remote -v` | Lista remotos configurados |
| `git remote remove <nombre>` | Quita el vínculo |
| `git push -u origin main` | Empuja y establece tracking |
| `git push` | Empuja la rama actual al remoto |

> **¿Qué hace `-u` (`--set-upstream`)?** Le dice a Git: "esta rama local va a seguir a esa rama remota". Después de eso, basta con `git push` y `git pull`, sin especificar destino.

#### Autenticación: HTTPS vs SSH

- **HTTPS:** usa usuario + token personal (PAT). Configuración rápida, pero pide credenciales seguido si no usa un credential helper.
- **SSH:** usa par de llaves criptográficas. Configuración inicial más larga, pero después es transparente.

Para una práctica, HTTPS está bien. Para trabajo profesional, SSH es el estándar.

**Generar llave SSH (configuración única):**

```bash
ssh-keygen -t ed25519 -C "[email protected]"
# Acepte la ubicación por defecto, ponga (o no) passphrase
cat ~/.ssh/id_ed25519.pub
# Copie ese contenido y péguelo en:
# GitHub → Settings → SSH and GPG keys → New SSH key
```

#### Ejercicio 7.1: Crear repositorio remoto y subir el local

**Enunciado:**

1. Cree un repositorio en GitHub llamado `practica-git`, vacío (sin README ni .gitignore).
2. Vincule su repositorio local con ese remoto.
3. Suba todas sus ramas y tags al remoto.
4. Verifique en GitHub que aparecen sus commits, ramas y tags.

**Solución:**

```bash
# 2
git remote add origin https://github.com/su-usuario/practica-git.git
git remote -v

# 3 - subir rama main
git push -u origin main

# subir todas las ramas
git push --all origin

# subir todos los tags
git push --tags origin

# 4 - abra el navegador y verifique
```

---

### Sección 8: `git pull`, `git push`, `git fetch`

#### Conceptos

| Comando | Qué hace |
|---------|----------|
| `git fetch` | Descarga del remoto los cambios, **sin aplicarlos** a su rama. Solo actualiza las "referencias remotas". |
| `git pull` | Es `git fetch` + `git merge` automático. |
| `git push` | Sube los commits de su rama al remoto. |

#### ¿Por qué `fetch` separado de `merge`?

Porque a veces usted quiere **inspeccionar** qué cambió en el remoto antes de fusionarlo. Si hace `pull` directo, Git fusiona sin preguntar. Si hace `fetch`, puede:

```bash
git fetch origin
git log HEAD..origin/main           # ver qué commits trae el remoto
git diff HEAD..origin/main          # ver el contenido de esos cambios
git merge origin/main               # decidir conscientemente fusionarlos
```

#### `pull` con rebase

```bash
git pull --rebase
```

En lugar de hacer merge (que crea un commit de merge), reaplica sus commits locales **encima** de los del remoto. Resultado: historia lineal, más limpia. Pero **no use rebase en commits ya compartidos**: misma regla que `reset`.

#### Ejercicio 8.1: Sincronización básica

**Enunciado:**

1. Desde GitHub (interfaz web), edite directamente el archivo `README.md` y haga commit.
2. En su máquina local, **sin haber sincronizado todavía**, también edite `README.md` (otra línea distinta) y haga commit.
3. Intente hacer `git push`. Observe el error.
4. Use `git fetch` para ver qué hay en el remoto.
5. Decida si hacer `git pull` (merge) o `git pull --rebase`.
6. Resuelva el conflicto si aparece.
7. Haga `push` exitoso.

**Solución:**

```bash
# 3 - error esperado:
# ! [rejected]        main -> main (fetch first)
# error: failed to push some refs...
# hint: Updates were rejected because the remote contains work that you do not have locally.

# 4
git fetch origin
git log --oneline --all --graph
# Verá la divergencia: dos ramas paralelas

# 5 - opción rebase
git pull --rebase
# o opción merge tradicional:
# git pull

# 6 - resuelva conflicto si aparece (igual que en sección 5)

# 7
git push
```

**Explicación:** El rechazo del push es una protección de Git: no le permite sobrescribir trabajo del remoto. Tiene que integrar primero los cambios remotos a su rama local, y luego sí empujar.

---

### Sección 9: Pull Requests y colaboración

#### Conceptos

Un **Pull Request (PR)** es una solicitud formal de fusionar una rama en otra, dentro de una plataforma como GitHub. Sirve para:

- **Revisión de código:** otros pueden comentar línea por línea.
- **Discusión:** se documenta el por qué del cambio.
- **Validación automática:** ejecutar tests, linters, builds (CI/CD).
- **Trazabilidad:** queda un registro de qué cambió, cuándo, quién aprobó.

> **PR vs Merge directo:** En proyectos serios, nadie hace `git push origin main` directo. Se trabaja en una rama, se abre un PR, se revisa y se fusiona. Esto se asegura con **branch protection rules** en GitHub.

#### Flujo típico de colaboración

1. Clonar el repositorio.
2. Crear una rama de feature.
3. Hacer commits y push de la rama.
4. Abrir un Pull Request en GitHub.
5. Recibir comentarios → ajustar → push (el PR se actualiza solo).
6. Aprobación.
7. Merge (en GitHub) → eliminar rama de feature.

#### Comandos clave de colaboración

| Comando | Uso |
|---------|-----|
| `git clone <url>` | Copia un repositorio remoto a su máquina |
| `git fetch origin` | Trae cambios sin fusionar |
| `git pull` | Trae y fusiona |
| `git push origin feature/x` | Sube su rama al remoto |
| `git branch -d feature/x` | Elimina rama local fusionada |
| `git push origin --delete feature/x` | Elimina rama remota |

#### Ejercicio 9.1: Colaboración entre dos compañeros

**Enunciado:**

Trabaje con un compañero. Uno será **Propietario** (P) y el otro **Colaborador** (C).

**Configuración:**

1. **P:** crea un repositorio público en GitHub llamado `colab-practica` con un README inicial.
2. **P:** invita a **C** desde **Settings → Collaborators**.
3. **C:** acepta la invitación desde su correo o desde notificaciones de GitHub.

**Trabajo en paralelo:**

4. **C:** clona el repositorio en su máquina:

   ```bash
   git clone https://github.com/usuario-P/colab-practica.git
   cd colab-practica
   ```

5. **C:** crea la rama `feature/seccion-instalacion`, agrega una sección al README explicando cómo instalar el proyecto, hace commit y push:

   ```bash
   git checkout -b feature/seccion-instalacion
   # editar README.md
   git add README.md
   git commit -m "Agrega sección de instalación al README"
   git push -u origin feature/seccion-instalacion
   ```

6. **C:** desde GitHub, abre un Pull Request de `feature/seccion-instalacion` hacia `main`.

7. **P:** recibe el PR, lo revisa, deja un comentario solicitando un cambio (por ejemplo: "agregar requisitos previos").

8. **C:** ajusta localmente, commitea y pushea de nuevo. El PR se actualiza automáticamente.

9. **P:** aprueba el PR y hace **Merge pull request** desde GitHub.

10. **C:** sincroniza su `main` local:

    ```bash
    git checkout main
    git pull
    git branch -d feature/seccion-instalacion
    git push origin --delete feature/seccion-instalacion
    ```

**Reflexión:** Note que en ningún momento **C** empujó directamente a `main`. Todo pasó por revisión. Este es el flujo profesional. Para reforzarlo, **P** puede activar **Branch Protection Rules** en `Settings → Branches → Add rule` y exigir revisión obligatoria.

---

## Parte 3: Markdown — Portada de perfil de GitHub

### Conceptos

GitHub permite crear un **README especial** que se muestra en la portada de su perfil público. Funciona así:

1. Cree un repositorio cuyo **nombre sea exactamente igual a su nombre de usuario de GitHub**.
2. Agregue un archivo `README.md` en la raíz.
3. Ese contenido aparecerá en `https://github.com/su-usuario`.

### Sintaxis Markdown esencial

```markdown
# Encabezado 1
## Encabezado 2
### Encabezado 3

**negrita**, *cursiva*, ~~tachado~~, `código en línea`

- lista
- con
- viñetas

1. lista
2. numerada

[texto del enlace](https://ejemplo.com)
![texto alternativo](url-de-imagen.png)

> Cita en bloque

| Columna 1 | Columna 2 |
|-----------|-----------|
| dato      | dato      |

---

​```python
def hola():
    print("Hola mundo")
​```
```

### Recursos visuales útiles para perfiles

- **Shields.io:** badges para tecnologías, sociales, contadores. `https://shields.io`
- **GitHub Stats:** tarjetas con estadísticas. `https://github.com/anuraghazra/github-readme-stats`
- **Iconos de tecnologías:** `https://devicon.dev` o `https://simpleicons.org`

### Ejercicio 10.1: Portada de perfil profesional

**Enunciado:**

Construya su README de perfil con las siguientes secciones, en orden:

1. **Encabezado** con su nombre y un saludo.
2. **Sobre mí**: 2-3 líneas describiendo sus intereses técnicos.
3. **Stack tecnológico** mostrado con badges.
4. **Lo que estoy aprendiendo** ahora mismo.
5. **Estadísticas de GitHub** (usar `github-readme-stats`).
6. **Contacto**: enlaces a LinkedIn, correo, portafolio.

**Solución (plantilla — adáptela a su información real):**

```markdown
<h1 align="center">¡Hola! Soy Su Nombre 👋</h1>

<p align="center">
  Estudiante de Ingeniería en Sistemas — apasionado por bases de datos, sistemas operativos y desarrollo de software.
</p>

---

## 🧑‍💻 Sobre mí

- 🎓 Cursando Ingeniería en Sistemas en [Su Universidad].
- 💡 Me interesa el desarrollo backend, las arquitecturas distribuidas y la administración de sistemas Linux.
- 🌎 Desde Guatemala.

## 🛠️ Stack tecnológico

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/-MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![Linux](https://img.shields.io/badge/-Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/-Git-F05032?style=flat&logo=git&logoColor=white)

## 📚 Aprendiendo actualmente

- Diseño de APIs REST con FastAPI.
- Containerización con Docker.
- Patrones de arquitectura de software.

## 📊 Mis estadísticas en GitHub

![Stats](https://github-readme-stats.vercel.app/api?username=su-usuario&show_icons=true&theme=default)
![Lenguajes](https://github-readme-stats.vercel.app/api/top-langs/?username=su-usuario&layout=compact)

## 📫 Contacto

- LinkedIn: [linkedin.com/in/su-perfil](https://linkedin.com/in/su-perfil)
- Correo: [[email protected]](mailto:[email protected])
- Portafolio: [su-portafolio.com](https://su-portafolio.com)

---

<p align="center">⭐ ¡Gracias por visitar mi perfil!</p>
```

**Pasos para publicarlo:**

```bash
# Cree el repositorio en GitHub con nombre EXACTAMENTE igual a su usuario
# Ejemplo: si su usuario es "rgomez99", el repo se llama "rgomez99"

git clone https://github.com/su-usuario/su-usuario.git
cd su-usuario
# cree el README.md con el contenido de arriba
git add README.md
git commit -m "Crea portada de perfil"
git push origin main
```

Una vez subido, visite `https://github.com/su-usuario` y verá la portada renderizada.

---

## Entregables

Para considerar completada la práctica, deberá entregar:

1. **Enlace al repositorio `practica-git`** en GitHub, con:
   - Al menos 10 commits con mensajes descriptivos.
   - Al menos 2 ramas adicionales a `main` (pueden estar fusionadas y eliminadas, deben verse en el `git log --all`).
   - Al menos 2 tags anotados.
   - Evidencia de un conflicto resuelto (mensaje de commit del merge).
2. **Enlace al repositorio `colab-practica`** del Ejercicio 9.1, con al menos un Pull Request fusionado por usted o por su compañero.
3. **Enlace a su perfil de GitHub** con la portada del Ejercicio 10.1 visible.
4. **Un documento PDF** (puede ser exportado desde el README) con:
   - Capturas del `git log --oneline --graph --all` final.
   - Una reflexión personal de máximo media página: ¿en qué momento de la práctica entendió mejor la diferencia entre `reset` y `revert`? ¿Qué dificultad encontró en la resolución de conflictos?

---

## Criterios de evaluación

Su práctica será evaluada considerando:

- **Comprensión conceptual:** los mensajes de commit y la reflexión final demuestran entendimiento, no copia mecánica.
- **Aplicación correcta de comandos:** evidencia en el historial de que se usaron las herramientas adecuadas para cada caso.
- **Calidad del flujo de trabajo:** uso de ramas, mensajes claros, ausencia de commits del tipo "fix", "asdf" o "cambios".
- **Colaboración efectiva:** el Pull Request muestra revisión real, no solo un merge instantáneo.
- **Presentación:** el README de perfil está pulido y refleja profesionalismo.

---

## Recursos complementarios

- **Documentación oficial de Git:** [git-scm.com/doc](https://git-scm.com/doc)
- **Pro Git book (gratuito):** [git-scm.com/book/es/v2](https://git-scm.com/book/es/v2)
- **Visualizador interactivo de Git:** [learngitbranching.js.org](https://learngitbranching.js.org)
- **GitHub Docs:** [docs.github.com](https://docs.github.com)
- **Markdown Guide:** [www.markdownguide.org](https://www.markdownguide.org)
