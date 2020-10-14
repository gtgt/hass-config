#include "esphome.h"
#include "esphome/components/thermostat/thermostat_climate.h"

class RoomThermostatClimate : public thermostat::ThermostatClimate {
 public:
  ClimateTraits traits() override {
    // The capabilities of the climate device
    auto traits = ThermostatClimate::traits();
    traits.set_supports_current_temperature(true);
    traits.set_supports_auto_mode(true);
    return traits;
  }
};
