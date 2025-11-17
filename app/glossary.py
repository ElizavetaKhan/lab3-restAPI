from typing import Dict
from .models import Entry

glossary: Dict[str, Entry] = {
    "usability_test": Entry(
        name="usability_test",
        description="метод оценки удобства использования интерфейса путем наблюдения за реальными пользователями.",
        reference="https://ru.wikipedia.org/wiki/%D0%AE%D0%B7%D0%B0%D0%B1%D0%B8%D0%BB%D0%B8%D1%82%D0%B8-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5"
    ),
    "heuristic_evaluation": Entry(
        name="heuristic_evaluation",
        description="экспертный анализ интерфейса по набору правил или принципов (эвристик).",
        reference="https://dsgners.ru/bikbye/3136-evristicheskaya-otsenka-moschnyiy-ux-instrument-v-rukah-dizaynera"
    ),
    "a_b_testing": Entry(
        name="a_b_testing",
        description="метод сравнения двух версий интерфейса, чтобы определить, какая лучше выполняет задачу пользователя.",
        reference="https://ru.wikipedia.org/wiki/A/B-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5"
    ),
}