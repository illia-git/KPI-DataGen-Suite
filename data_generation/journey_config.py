# Configurations for journeys and car models
CAR_MODELS = ["skoda-model-1", "skoda-model-2", "skoda-model-3"]

JOURNEYS = ["Car Configurator", "Dealer Search", "Inventory Check", "Brandportal"]

STEPS = {
    "Car Configurator": ["car-configurator.start", "car-configurator.step-1", "car-configurator.step-2", "car-configurator.finish"],
    "Dealer Search": ["dealer-search.dealer-1", "dealer-search.dealer-2", "dealer-search.finish"],
    "Inventory Check": ["inventory-check.skoda-model-1", "inventory-check.skoda-model-2", "inventory-check.booking"],
    "Brandportal": ["brandportal.skoda-model-1", "brandportal.skoda-model-2", "brandportal.finish"]
}
