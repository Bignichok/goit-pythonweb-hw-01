import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Основна функція програми"""
    logger.info("Програма запущена!")


if __name__ == "__main__":
    main()
