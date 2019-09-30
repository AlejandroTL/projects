/**
  ******************************************************************************
  * File Name          : main.c
  * Description        : Main program body
  ******************************************************************************
  * This notice applies to any and all portions of this file
  * that are not between comment pairs USER CODE BEGIN and
  * USER CODE END. Other portions of this file, whether 
  * inserted by the user or by software development tools
  * are owned by their respective copyright owners.
  *
  * Copyright (c) 2018 STMicroelectronics International N.V. 
  * All rights reserved.
  *
  * Redistribution and use in source and binary forms, with or without 
  * modification, are permitted, provided that the following conditions are met:
  *
  * 1. Redistribution of source code must retain the above copyright notice, 
  *    this list of conditions and the following disclaimer.
  * 2. Redistributions in binary form must reproduce the above copyright notice,
  *    this list of conditions and the following disclaimer in the documentation
  *    and/or other materials provided with the distribution.
  * 3. Neither the name of STMicroelectronics nor the names of other 
  *    contributors to this software may be used to endorse or promote products 
  *    derived from this software without specific written permission.
  * 4. This software, including modifications and/or derivative works of this 
  *    software, must execute solely and exclusively on microcontroller or
  *    microprocessor devices manufactured by or for STMicroelectronics.
  * 5. Redistribution and use of this software other than as permitted under 
  *    this license is void and will automatically terminate your rights under 
  *    this license. 
  *
  * THIS SOFTWARE IS PROVIDED BY STMICROELECTRONICS AND CONTRIBUTORS "AS IS" 
  * AND ANY EXPRESS, IMPLIED OR STATUTORY WARRANTIES, INCLUDING, BUT NOT 
  * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
  * PARTICULAR PURPOSE AND NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY
  * RIGHTS ARE DISCLAIMED TO THE FULLEST EXTENT PERMITTED BY LAW. IN NO EVENT 
  * SHALL STMICROELECTRONICS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
  * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
  * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
  * OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
  * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
  * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
  * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  *
  ******************************************************************************
  */

/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "stm32f0xx_hal.h"
#include "cmsis_os.h"

/* USER CODE BEGIN Includes */
#include "fsm.h"
#include "task.h"
/* USER CODE END Includes */

/* Private variables ---------------------------------------------------------*/
osThreadId defaultTaskHandle;

/* USER CODE BEGIN PV */
/* Private variables ---------------------------------------------------------*/
uint32_t tiempo_general;
int n = 0;
int digit = 0;
int code = 0;


/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
void StartDefaultTask(void const * argument);

/* USER CODE BEGIN PFP */
/* Private function prototypes -----------------------------------------------*/

xTaskHandle startLightTask_Handle;
void startLightTask();

/* FSM functions */
/* Guard functions */
//int pulsado(fsm_t* this);
/* Output functions */
void encender(fsm_t* this);
void apagar(fsm_t* this);

/* USER CODE END PFP */

/* USER CODE BEGIN 0 */
enum light_state {OFF, ON, };
enum alarma_state {DESARMADA, ARMADA, ALARMA };
enum code_state {IDLE, COUNT1, CHECK1, COUNT2, CHECK2, COUNT3, CHECK3};

void apagar(fsm_t* this) {
	HAL_GPIO_TogglePin(GPIOC, LD4_Pin); //Toggle the state of pin PC8
}

void encender(fsm_t* this) {
	HAL_GPIO_TogglePin(GPIOC, LD4_Pin); //Toggle the state of pin PC8
}

void code_ok(fsm_t* this){
	code = 1;
}

int pulsado_light (fsm_t* this) {
	if ((HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_1)==1)){ //|| (HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0)==1) ){
	  tiempo_general = HAL_GetTick();
	  return 1;
  } else {
	  return 0;
  }

}

int intrusion (fsm_t* this) {
	if ((HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_10)==1)){
		return 1;
	} else {
		return 0;
	}
}

int check_code (fsm_t* this) {
	if (code==1){
		code = 0;
		return 1;
	} else {
		return 0;
	}

}

int pulsado(fsm_t* this) {
	if (HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0)==1){
	  //tiempo_general = HAL_GetTick();
	  return 1;
  } else {
	  return 0;
  }
}


void contar (fsm_t* this) {
	n++;
}


int transition (fsm_t* this) {

	static uint32_t tiempo_propio;
	tiempo_propio = HAL_GetTick();

	if ((tiempo_propio - tiempo_general) > 1000){
		return 1;
	} else {
		return 0;
	}

}

void trans_blank (fsm_t* this) {
	digit = n;
	n = 0;
}

int right1 (fsm_t* this) {

	int key1 = 2;

	if (digit == key1) {
		return 1;
	} else {
		return 0;
	}

}

int error1 (fsm_t* this) {

	int key1 = 2;

	if (digit == key1) {
		return 0;
	} else {
		return 1;
	}

}

int right2 (fsm_t* this) {

	int key2 = 3;

	if (digit == key2) {
		return 1;
	} else {
		return 0;
	}

}

int error2 (fsm_t* this) {

	int key2 = 3;

	if (digit == key2) {
		return 0;
	} else {
		return 1;
	}

}

int right3 (fsm_t* this) {

	int key3 = 4;

	if (digit == key3) {
		return 1;
	} else {
		return 0;
	}

}

int error3 (fsm_t* this) {

	int key3 = 4;

	if (digit == key3) {
		return 0;
	} else {
		return 1;
	}

}

int temporizado(fsm_t* this) {

	static uint32_t tiempo_propio;
	tiempo_propio = HAL_GetTick();

	if ((tiempo_propio - tiempo_general) > 1000){
		return 1;
	} else {
		return 0;
	}
}


void alarma (fsm_t* this) {
	HAL_GPIO_WritePin(GPIOC, LD3_Pin, 1);
}

void alarma_off (fsm_t* this) {
	HAL_GPIO_WritePin(GPIOC, LD3_Pin, 0);
}



static fsm_trans_t alarma_tt[] = {
  { DESARMADA, check_code, ARMADA, NULL },
  { ARMADA, intrusion, ALARMA, alarma },
  { ARMADA, check_code, DESARMADA, NULL },
  { ALARMA, intrusion, DESARMADA, alarma_off },
  { -1, NULL, -1, NULL },
};

static fsm_trans_t light_tt[] = {
  { OFF, pulsado_light, ON, encender },
  { ON, transition, OFF, apagar },
  { -1, NULL, -1, NULL },
};

static fsm_trans_t code_tt[] = {
  { IDLE, pulsado, COUNT1, contar },
  { COUNT1, pulsado, COUNT1, contar },
  { COUNT1, transition, CHECK1, trans_blank },
  { CHECK1, right1, COUNT2, trans_blank },
  { CHECK1, error1, IDLE, trans_blank },
  { COUNT2, pulsado, COUNT2, contar },
  { COUNT2, transition, CHECK2, trans_blank },
  { CHECK2, right2, COUNT3, trans_blank },
  { CHECK2, error2, IDLE, trans_blank },
  { COUNT3, pulsado, COUNT3, contar },
  { COUNT3, transition, CHECK3, trans_blank },
  { CHECK3, right3, IDLE, code_ok },
  { CHECK3, error3, IDLE, trans_blank },
  { -1, NULL, -1, NULL },
};

/* USER CODE END 0 */

int main(void)
{

  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration----------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();

  /* USER CODE BEGIN 2 */



  /* USER CODE END 2 */

  /* USER CODE BEGIN RTOS_MUTEX */
  /* add mutexes, ... */
  /* USER CODE END RTOS_MUTEX */

  /* USER CODE BEGIN RTOS_SEMAPHORES */
  /* add semaphores, ... */
  /* USER CODE END RTOS_SEMAPHORES */

  /* USER CODE BEGIN RTOS_TIMERS */
  /* start timers, add new ones, ... */

  xTaskCreate(startLightTask, "startLightTask", 128, NULL, 3, &startLightTask_Handle);
  /* USER CODE END RTOS_TIMERS */

  /* Create the thread(s) */
  /* definition and creation of defaultTask */
  osThreadDef(defaultTask, StartDefaultTask, osPriorityNormal, 0, 128);
  defaultTaskHandle = osThreadCreate(osThread(defaultTask), NULL);

  /* USER CODE BEGIN RTOS_THREADS */
  /* add threads, ... */
  /* USER CODE END RTOS_THREADS */

  /* USER CODE BEGIN RTOS_QUEUES */
  /* add queues, ... */
  /* USER CODE END RTOS_QUEUES */
 

  /* Start scheduler */
  osKernelStart();
  
  /* We should never get here as control is now taken by the scheduler */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
  /* USER CODE END WHILE */

  /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */

}

/** System Clock Configuration
*/
void SystemClock_Config(void)
{

  RCC_OscInitTypeDef RCC_OscInitStruct;
  RCC_ClkInitTypeDef RCC_ClkInitStruct;

    /**Initializes the CPU, AHB and APB busses clocks 
    */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = 16;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL12;
  RCC_OscInitStruct.PLL.PREDIV = RCC_PREDIV_DIV1;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

    /**Initializes the CPU, AHB and APB busses clocks 
    */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_1) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

    /**Configure the Systick interrupt time 
    */
  HAL_SYSTICK_Config(HAL_RCC_GetHCLKFreq()/1000);

    /**Configure the Systick 
    */
  HAL_SYSTICK_CLKSourceConfig(SYSTICK_CLKSOURCE_HCLK);

  /* SysTick_IRQn interrupt configuration */
  HAL_NVIC_SetPriority(SysTick_IRQn, 3, 0);
}

/** Configure pins as 
        * Analog 
        * Input 
        * Output
        * EVENT_OUT
        * EXTI
*/
static void MX_GPIO_Init(void)
{

  GPIO_InitTypeDef GPIO_InitStruct;

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOC, GPIO_PIN_6|LD4_Pin|LD3_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : PC3 */
  GPIO_InitStruct.Pin = GPIO_PIN_10;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

  /*Configure GPIO pins : PA0 PA1 */
  GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_RISING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pins : PC6 LD4_Pin LD3_Pin */
  GPIO_InitStruct.Pin = GPIO_PIN_6|LD4_Pin|LD3_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

  /* EXTI interrupt init*/
  HAL_NVIC_SetPriority(EXTI0_1_IRQn, 3, 0);
  HAL_NVIC_EnableIRQ(EXTI0_1_IRQn);

}

/* USER CODE BEGIN 4 */
void startLightTask()
{

  TickType_t xLastWakeTime;
  // Task activation period is 1s.
  const TickType_t xFrequency = 250 / portTICK_PERIOD_MS;

  fsm_t*  code_fsm = fsm_new(code_tt);
  fsm_t*  light_fsm = fsm_new(light_tt);
  fsm_t*  alarma_fsm = fsm_new(alarma_tt);

  // Initialise the xLastWakeTime variable with the current time.
  xLastWakeTime = xTaskGetTickCount();
  while(1){

  //set_frequency(HSE)    //ESTA NO ES LA FUNCION REAL A UTILIZAR
			  //Lo correcto sería cambiar el reloj a HSE, pero no tengo Cube en el momento de realizar la practica y no me se la funcion de memoria para cambiarlo.
			  //Se que es cambiando parametros de la funcion void SystemClock_Config(void); pero estoy programando desde Gedit y no me la juego a tocar algo y tocarlo mal, prefiero encapsular todo eso en la funcion comentada.
    fsm_fire(code_fsm);
    fsm_fire(light_fsm);
    fsm_fire(alarma_fsm);

    // Block task until next activation is due.
    vTaskDelayUntil(&xLastWakeTime, xFrequency);
  }
}
/* USER CODE END 4 */

/* StartDefaultTask function */
void StartDefaultTask(void const * argument)
{

  /* USER CODE BEGIN 5 */
  /* Infinite loop */
  for(;;)
  {
    osDelay(1);
  }
  /* USER CODE END 5 */ 
}

/**
  * @brief  Period elapsed callback in non blocking mode
  * @note   This function is called  when TIM1 interrupt took place, inside
  * HAL_TIM_IRQHandler(). It makes a direct call to HAL_IncTick() to increment
  * a global variable "uwTick" used as application time base.
  * @param  htim : TIM handle
  * @retval None
  */
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
/* USER CODE BEGIN Callback 0 */

/* USER CODE END Callback 0 */
  if (htim->Instance == TIM1) {
    HAL_IncTick();
  }
/* USER CODE BEGIN Callback 1 */

/* USER CODE END Callback 1 */
}

/**
  * @brief  This function is executed in case of error occurrence.
  * @param  None
  * @retval None
  */
void _Error_Handler(char * file, int line)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  while(1) 
  {
  }
  /* USER CODE END Error_Handler_Debug */ 
}

#ifdef USE_FULL_ASSERT

/**
   * @brief Reports the name of the source file and the source line number
   * where the assert_param error has occurred.
   * @param file: pointer to the source file name
   * @param line: assert_param error line source number
   * @retval None
   */
void assert_failed(uint8_t* file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
    ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */

}

#endif

/**
  * @}
  */ 

/**
  * @}
*/ 

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
